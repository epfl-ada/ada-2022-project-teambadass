# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from scipy import stats
from datetime import datetime as dt

from PIL import Image, ImageDraw
from matplotlib.offsetbox import AnnotationBbox, OffsetImage


# data analysis
def bootstrap_CI(data, num_draws=10000, metric=np.nanmean):
    """
    Computes 95% confidence interval
    Parameters
    ----------
    data: array_like
        The data you desire to calculate confidence interval for
    num_draws: int
        Number of draws to be used for the computation of the CI. The default value is set to 10000
    Returns
    -------
    ndarray
        An array containing the 2.5 percentile at index 0 and the 97.5 percentile at index 1
    """
    means = np.zeros(num_draws)
    data = np.array(data)
    N = len(data)

    for n in range(num_draws):
        data_tmp = np.random.choice(data, N)
        means[n] = metric(data_tmp)

    return [np.nanpercentile(means, 2.5), np.nanpercentile(means, 97.5)]


def check_summary(summary, list_):
    """
    Count what proportion of words from a list the summary contains

    Parameters
    ----------
    summary: string
        The summary you desire to check
    list_: array
        The list to do look up in

    Returns
    -------
    int
        Proportion of words contained from given list (0-1)
    """
    cnt = 0
    summary_lst = summary.lower().split()
    for word in summary_lst:
        if word in list_:
            cnt += 1
    return cnt / len(summary_lst)


# data processing
def correct_for_inflation(
    movies,
    inflation_data_path,
    capital_col,
    release_col="movie_release_date",
    start_year=2000,
    end_year=2012,
):
    """
    Corrects for inflation in input DataFrame. All values will be corrected
    with start_year as base case
    Args:
            movies: DataFrame
                    The movies containing values that are to be corrected for
                    inflation
            capital_col: String
                    The column that needs to be corrected for inflation. Ex:
                    'box_office_revenue'
            release_col: String
                    The column name of release date in the input DataFrame
            inflation_data_path: String
                    Data path to where inflation data set is located
            start_year: int
                    Denoting start year which should be corrected
            end_year: int
                    Denoting end year which should be corrected
    Returns:
            df: DataFrame
                    DataFrame that has been corrected for inflation
    """

    # load inflation data
    inflation = pd.read_csv(inflation_data_path, header=2)

    # we only need the data for United Stated (country code USA)
    inflation = inflation.loc[inflation["Country Code"] == "USA"]

    years = [str(i) for i in range(start_year, end_year + 1)]

    # only include inflation data from start_year to end_year
    inflation = inflation[years]

    # create index multipliers for every year from start_year to end_year
    # prices will be indexed to start_year prices
    inflation[str(start_year)] = 1
    for i in range(len(years) - 1):
        inflation[years[i + 1]] = inflation[years[i]] * (
            1 + inflation[years[i + 1]] / 100
        )

    # Make a copy of movies to avoid changing the input DataFrame
    movies_copy = movies.copy(deep=True)

    # Correcting movie revenue corresponding to movie year
    for i in range(len(years) - 1):
        movies_copy.loc[
            (movies_copy[release_col] >= years[i])
            & (movies_copy[release_col] < years[i + 1]),
            capital_col,
        ] /= inflation.iloc[0][years[i]]

    return movies_copy


def get_path(url):
    """
    Returns data path for input url.
    Returned path can be used to make dataframe.

    Parameters
    ----------
    url: string
        The url you desire to find path for

    Returns
    -------
    path: string
        The path which can be used to make dataframe in pandas

    """
    return "https://drive.google.com/uc?id=" + url.split("/")[-2]


def is_given_date(x, format_="%Y-%m-%d"):
    """
    Returns if the complete date were given or only the year.

    Parameters
    ----------
    x: array-like
        array-like object containing the dates
    format_ : string
        the format for a complete date

    Returns
    -------
    res: boolean
        True if the date is complete and false otherwise
    """
    try:
        res = bool(dt.strptime(x, format_))
    except ValueError:
        res = False
    return res


def bootstrap_mean_diff_CI(data1, data2, num_draws=10000):
    """
    Computes 95% confidence interval for the mean difference between data1 and data2
    Parameters
    ----------
    data1: array_like
        The data you desire to calculate confidence interval for
    data2: array_like
        The data you desire to calculate confidence interval for
    num_draws: int
        Number of draws to be used for the computation of the CI. The default value is set to 10000
    Returns
    -------
    ndarray
        An array containing the 2.5 percentile at index 0 and the 97.5 percentile at index 1
    """
    means = np.zeros(num_draws)
    data1 = np.array(data1)
    data2 = np.array(data2)
    N1 = len(data1)
    N2 = len(data2)

    for n in range(num_draws):
        data1_tmp = np.random.choice(data1, N1)
        data2_tmp = np.random.choice(data2, N2)
        means[n] = np.nanmean(data1_tmp) - np.nanmean(data2_tmp)

    return [np.nanpercentile(means, 2.5), np.nanpercentile(means, 97.5)]


def bootstrap_ttest_CI(data1, data2, num_draws=10000):
    """
    Computes 95% confidence interval for the ttest between data1 and data2
    Parameters
    ----------
    data1: array_like
        The data you desire to calculate confidence interval for
    data2: array_like
        The data you desire to calculate confidence interval for
    num_draws: int
        Number of draws to be used for the computation of the CI. The default value is set to 10000
    Returns
    -------
    ndarray
        An array containing the 2.5 percentile at index 0 and the 97.5 percentile at index 1
    """
    pvals = np.zeros(num_draws)
    data1 = np.array(data1)
    data2 = np.array(data2)
    N1 = len(data1)
    N2 = len(data2)

    for n in range(num_draws):
        data1_tmp = np.random.choice(data1, N1)
        data2_tmp = np.random.choice(data2, N2)
        pvals[n] = stats.ttest_ind(data1_tmp, data2_tmp)[1]

    return [np.nanpercentile(pvals, 2.5), np.nanpercentile(pvals, 97.5)]


def score_to_categories(score):
    """
    Divides a continous value into 5 categories.
    Args:
        score: float
            The score to be divided into categories.
    Returns:
        str
            The category the score belongs to.
    """
    if score <= 0.2:
        return "(0-0.2]"
    elif score <= 0.4:
        return "(0.2-0.4]"
    elif score <= 0.6:
        return "(0.4-0.6]"
    elif score <= 0.8:
        return "(0.6-0.8]"
    else:
        return "(0.8-1]"


# helper ro get the number of elements in a dictionary
def get_num_elements(str_dict):
    """Get the number of elements in a dictionary
    Args:
        str_dict: str
            String representation of a dictionary
    Returns:
        int
            Number of elements in the dictionary
    """
    return len(str_dict.split(","))


# helper to compare to propensity scores
def get_similarity(propensity_score1, propensity_score2):
    """Calculate similarity for instances with given propensity scores
    Args:
        propensity_score1: float
            Propensity score for instance 1
        propensity_score2: float
            Propensity score for instance 2
    Returns:
        float
            Similarity between the two instances
    """
    return 1 - np.abs(propensity_score1 - propensity_score2)


# helper to check if two dictionaries share a value
def shared_value(dict1, dict2):
    """
    Check if two dictionaries share a value
    Args:
        dict1: dict
            Dictionary with values to be compared
        dict2: dict
            Dictionary with values to be compared
    Returns:
        bool:
            True if there is a shared value, False otherwise
    """
    list1 = list(dict1.values())
    for genre in dict2.values():
        if genre in list1:
            return True


def get_ab_from_actor(node, node_sizes, pos):
    # read the image file for this node
    img = Image.open('./img/' + node.split('/m/')[0] + node.split('_ID_')[1].replace('/', ':') + '.jpg')

    h,w = img.size
    # Resize the image to a square shape
    side_length = min(h, w)
    # crop the image to a square
    img = img.crop(((h-side_length)//2, (w-side_length)//2, (h+side_length)//2, (w+side_length)//2))
    img = img.resize((800,800))
    h,w = img.size
    
    # creating luminous image
    lum_img = Image.new('L',[h,w] ,0) 
    draw = ImageDraw.Draw(lum_img)
    draw.pieslice([(0,0),(h,w)],0,360,fill=255)
    img_arr = np.array(img)
    lum_img_arr = np.array(lum_img)
    final_img_arr = np.dstack((img_arr, lum_img_arr))

    image = Image.fromarray(final_img_arr)
    
    # create an OffsetImage object for the image
    image_offset = OffsetImage(image, zoom=node_sizes[node]/2000000000) #, cmap=plt.cm.gray_r)
    
    # create an AnnotationBbox object for the image
    ab = AnnotationBbox(image_offset, pos[node], frameon=False)
    
    return ab