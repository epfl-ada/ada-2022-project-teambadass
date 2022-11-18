# The recipe for a movie success 
## Abstract
The global film industry is a [`$`100 billion worth industry](https://en.wikipedia.org/wiki/Film_industry). There is a vast potential to earn money, and the producers are willing to sacrifice considerable costs to become a movie success. `Pirates of the Caribbean: On Stranger Tides,` the most expensive film, cost [`$`379 million](https://en.wikipedia.org/wiki/List_of_most_expensive_films). With such an amount at your disposal, you may wonder what you should spend the money on. Should you use them to get one of the biggest movie stars in your cast? For many, this may be tempting. One of the most famous actors, `Tom Cruise,` was rewarded [`$`100,000,000](https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors) for his performance in `Top Gun: Maverick.` But was it worth it? Or could the money be better spent? The [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) contains data on the revenue of  8 401 movies. We will analyze this data to create a recipe for a successful movie.

## Research Questions
In our initial analysis, we define the success of a movie in terms of box office revenue. To create a recipe for the production of a successful film, we have limited ourselves to 5 main research questions:

1. Does the movie release date have a significant impact on the success of a film and if so, what is the optimal release date with respect to the time of the year? Subsequently, the question arises whether this result differs for different genres.
2. How do the gender ratio and the number of ethnicities in the cast affect the success of a movie?
3. Do certain actors have a significant positive or negative impact on the success of a movie?
4. Is the length of a movie related to its success and if so in what way?
5. Is the use of negatively connoted words, positively connoted words, and words related to violence in the movie plot related to the success of the movie?

In further analysis, we will extend the definition of a movie's success to include ratings. Subsequently, we will evaluate how our results change when we choose ratings as an indicator of success.


## Additional Datasets
- [**Budget**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv) - a dataset containing budget of movies. Budget is essential to reduce the risk of confounding variables when analyzing the relationship between our variables of interest and the box office revenue. We will merge this dataset with [**movie.metadata.csv**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link) by combining movie name, release year and runtime to create a unique key for each movie. 
- [**World Bank CPI**](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2012&start=1990&view=chart) - a dataset containing country names and inflation data will be used to adjust budgets and box office revenues of the movies. We use the Headline Consumer Price Index (CPI) of the United States to adjust for inflation. CPI is the most widely used measure of inflation, and we use the U.S. as a baseline because both budget and box office revenue are stated in USD. By adjusting for inflation, we can measure financial success in constant dollars, which allows us to compare movies from different years.
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - In addition to defining a movie successful in financial terms, we want to make the definition more diverse by measuring success in terms of ratings received as well. We have extracted two datasets from IMDb - one for making the merge with our movie data possible (movie name, release year and runtime), and one for extracting the average ratings and number of votes received.
- [**Vocabularies**](https://drive.google.com/drive/folders/1-KcpE8cju60CcNXWc_gPZ6x3V8r7T5eH?usp=share_link) ([**Positive**](https://ptrckprry.com/course/ssd/data/positive-words.txt), [**Negative**](https://ptrckprry.com/course/ssd/data/negative-words.txt), and [**Violence**](https://myvocabulary.com/word-list/violence-vocabulary/)) - We analyze the plot summaries in [**movie.metadata.csv**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link) from three sentiments: positive, negative and violent words and analyze if their proportion in the plot summaries affects revenue. 


## Methods

Spearman Correlation 
We used the Spearman correlation to test for a monotonic relation between various attributes and revenue. 

T-tests
We use t-tests to determine if there is a significant difference between the means of the two groups and how they are related. We simulate the t-tests 10 000 times to calculate the statistical power, and we used bootstrap with 10 000 draws to compute the 95% CI. The groups we have used for the t-tests will be clarified in the steps we describe. 

Linear Regression
We performed linear regression with ordinary least squares (OLS) to see the correlation between various attributes and revenue. In our initial analysis, we were particularly interested in R-squared to see how our models explain the revenue made. 

We describe our choice of methods using our research questions as a baseline. Further details on the steps we describe can be found in [**project_milestone_2.ipynb**](link) with the same structure as the following:

### Step 1: General Pre-Processing
Movie Metadata
We are looking for a recipe to maximize the movie box office revenue. We have therefore removed all movies without movie_box_office_revenue.
We adjust the budget and box_office_revenue for inflation as described in [**Additional datasets**](https://github.com/epfl-ada/ada-2022-project-teambadass/blob/main/README.md). For the current stage of the project, we decided to analyze movies going back to 1960, which is the first year we have data for inflation. 
Character Metadata
We removed characters without freebase_actor_ID.
We merged actors with movies on wikipedia_movie_ID to be able to explore how actors affect movie revenue

### Step 2: Release Date



### Step 3: Diversity
We used $ethnicity\ score = \frac{number\ of\ ethnicities}{number\ of\ actors}$ and $female\ score = \frac{number\ of\ females}{number\ of\ actors}$ to measure the effect of diversity on revenue made.

### Step 4: Cast
We used One-Hot Encoding of the actors by creating a dummy variable for each actor. We created a new variable for each actor, so we had to experiment with different thresholds to avoid excessively large DataFrames. The threshold corresponds to how many movies the actor has played. 
The DataFrame was then used in a linear regression model using the actors as categorical predictors. 
Later in the project, we want to include more predictors to reduce the chances of confounders. 

### Step 5: Runtime
We used runtime and box office revenue to split the DataFrames into pairwise groups. We performed t-tests to determine the difference in means between each pair. 

### Step 6: Plot Summary
We calculate the proportion of words with positive / negative / violent connotations out of all words in the movie summary. We use both t-tests and linear regression to measure the effect of certain words used to describe the movie. 

### Methods for the future
We want to continue exploring the methods we have used in our initial analysis. However, our current analysis might fail to account for confounding variables which could have caused them to wrongly estimate the relationship we have seen so far. We will use pair matching of movies to control for effects of confounding variables. We also want to perform trend analysis to see 


## Proposed timeline
```
.
├── 21.11.22 - Perform paired matching
│  
├── 23.11.22 - Perform trend analysis
│  
├── 25.11.22 - (Optional) Include IMDb rating
│  
├── 28.11.22 - Pause project work
│  
├── 02.12.22 - Homework 2 deadline
│    
├── 05.12.22 - Perform final analysis
│  
├── 12.12.22 - Develop draft for data story
│  
├── 15.12.22 - Finalize code implementations and visualizations
│  
├── 18.12.22 - Finalize data story
│  
├── 23.12.22 - Milestone 3 deadline
│  
├── 24.12.22 - Merry Christmas!
.

```

## Organization within the team 
<table class="tg" style="undefined;table-layout: fixed; width: 342px">
<colgroup>
<col style="width: 164px">
<col style="width: 178px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0lax"></th>
    <th class="tg-0lax">Tasks</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax">@anni5701</td>
    <td class="tg-0lax">Create meaningful visualizations<br><br>Continue exploring the dataset<br><br>Integrate IMDb rating</td>
  </tr>
  <tr>
    <td class="tg-0lax">@kevinxyc1</td>
    <td class="tg-0lax">Analyze successful movie themes<br><br>Create meaningful visualizations<br><br>Develop the web interface</td>
  </tr>
  <tr>
    <td class="tg-0lax">@olavseim</td>
    <td class="tg-0lax">Develop the web interface<br><br>Develop the final text for the data story<br><br>Perform trend analysis</td>
  </tr>
  <tr>
    <td class="tg-0lax">@torkelwestby</td>
    <td class="tg-0lax">Analyze successfull actors<br><br>Develop the final text for the data story<br><br>Perform paired matching</td>
  </tr>
</tbody>
</table>
