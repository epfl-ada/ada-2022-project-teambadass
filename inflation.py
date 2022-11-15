import pandas as pd

def correct_for_inflation(movies, column, start_year=2000, end_year=2012):	
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
	data_folder = './data/'
	inflation = pd.read_csv(data_folder + 'inflation.csv', header=2)

	# we only need the data for United Stated (country code USA)
	inflation = inflation.loc[inflation['Country Code']=='USA']
	
	years = [str(i) for i in range(start_year, end_year+1)]

	# only include inflation data from start_year to end_year
	inflation = inflation[years]

	# create index multipliers for every year from start_year to end_year
	# prices will be indexed to start_year prices
	inflation[str(start_year)] = 1
	for i in range(len(years) - 1):
		inflation[years[i+1]] = inflation[years[i]] * (1 + inflation[years[i+1]] / 100)
		
	# Make a copy of movies to avoid changing the input DataFrame
	movies_copy = movies.copy(deep=True)
		
	# Correcting movie revenue corresponding to movie year
	for i in range(len(years) - 1):
		movies_copy.loc[(movies_copy['release_date'] >= years[i]) \
				   & (movies_copy['release_date'] < years[i+1]), column] /= inflation.iloc[0][years[i]]
		
	return movies_copy