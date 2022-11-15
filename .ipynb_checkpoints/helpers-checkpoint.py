# -*- coding: utf-8 -*-

import numpy as np


def bootstrap_CI(data1, data2, num_draws=10000):
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


import pandas as pd


def correct_for_inflation(movies, column, start_year, end_year):
    """
    Corrects for inflation in input DataFrame. All values will be corrected with start_year as base case
    Args:
            movies: DataFrame
                    The movies containing values that are to be corrected for inflation
            column: string
                    The column that is to be corrected for inflation. Ex: 'box_office_revenue'
            start_year: int
                    Denoting start year which should be corrected
            end_year: int
                    Denoting end year which should be corrected
    Returns:
            df: DataFrame
                    The dataframe that has been corrected for inflation
    """

    # load inflation data
    data_folder = "./data/"
    inflation = pd.read_csv(data_folder + "inflation.csv", header=2)

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
            (movies_copy["movie_release_date"] >= years[i])
            & (movies_copy["movie_release_date"] < years[i + 1]),
            column,
        ] /= inflation.iloc[0][years[i]]

    return movies_copy
