# The recipe for a movie success 
## Abstract
The global film industry is a [`$`100 billion worth industry](https://en.wikipedia.org/wiki/Film_industry). There is a vast potential to earn money, and the producers are willing to sacrifice considerable costs to become a movie success. `Pirates of the Caribbean: On Stranger Tides,` the most expensive film, cost [`$`379 million](https://en.wikipedia.org/wiki/List_of_most_expensive_films). With such an amount at your disposal, you may wonder what you should spend the money on. Should you use them to get one of the biggest movie stars in your cast? For many, this may be tempting. One of the most famous actors, `Tom Cruise,` was rewarded [`$`100,000,000](https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors) for his performance in `Top Gun: Maverick.` But was it worth it? Or could the money be better spent? The [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) contains data on the revenue of  8 401 movies. We will analyze this data to create a recipe for a successful movie.

## Research Questions
In our intial analysis, we define the success of a film in terms of box office revenue. To create a recipe for the production of a successful film, we have limited ourselves to 5 main categories, which we will examine in more detail for their influence on the success of a film.

1. Do certain actors have an significant positive or negative impact on the movies success?
2. Do the day, month and year of a film's release date have a significant impact on the success of a film and if so, what is the optimal release date with respect to day and month? Subsequently, the question arises whether this result differs for different genres.
3. Is the length of a movie related to its success and if so in what way?
4. Is the use of negatively connoted words, positively connoted words and words related to violence in the plot of a movie related to the success of the movie?
5. Regarding the analysis of the actors, do the gender ratio of the actors and the number of ethnicities of the actors have an impact on the success of the movie?

In further analysis, we will extend the definition of a movie's success to include ratings. Subsequently, we will evaluate how our results change when we choose ratings as an indicator of success.

## Additional Datasets
- [**Budget**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv) - a dataset containing budget of movies. Budget is essential to reduce the risk of confounding variables when analyzing the relationship between our variables of interest and the box office revenue. 
- [**World Bank CPI**](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2012&start=1990&view=chart) - a dataset containing country names and inflation data will be used to adjust budgets and box office revenues of the movies. We use the Headline Consumer Price Index (CPI) of the United States to adjust for inflation. CPI is the most widely used measure of inflation, and we use the U.S. as a baseline because both budget and revenue are stated in USD in our datasets. By adjusting for inflation, we can measure financial success in constant dollars, which allows us to compare movies from different years. 
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - In addition to defining a movie successful in financial terms, we want to make the definition more diverse by measuring success in terms of ratings received as well. We have extracted two datasets from IMDb - one for making the merge with our movie data possible (movie name, release year and runtime), and one for extracting the average ratings and number of votes received.
- [**Vocabularies**](https://drive.google.com/drive/folders/1-KcpE8cju60CcNXWc_gPZ6x3V8r7T5eH?usp=share_link) ([**Positive**](https://ptrckprry.com/course/ssd/data/positive-words.txt), [**Negative**](https://ptrckprry.com/course/ssd/data/negative-words.txt), and [**Violence**](https://myvocabulary.com/word-list/violence-vocabulary/)) - We analyze the plot summaries in [**movie.metadata.csv**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link) from three sentiments: positive, negative and violent words and analyze if their proportion in the plot summaries affects revenue. 


## Methods

We utilized various methods in analyzing five main attributes of a movie (Diversity, Cast, Release Date, Runtime, Plot Summary) and how they may affect the revenue. Here are the methods and steps during our analysis.

### Data Preprocessing
- Movie Metadata
  - We are looking for a recipe to maximize the movie box office revenue. We have therefore removed all movies without movie_box_office_revenue.
  - We normalize the revenue by taking account into inflation between 1960 to 2014 so that movies are more comparable.
- Character Metadata
  - We removed characters without freebase_actor_ID to address for null id.
  - We merged actors with movies to be able to explore how actors affect movie revenue.
  - We implemented one hot encoded actors such that each actor corresponds to a column, and each row for that column is 1 if the actor played the movie. We also tried different thresholds for how many movies they had played for them to be included in the dataframe.

### Spearman Correlation
We used the Spearman correlation to test for a correlation between various attributes and revenue. The Spearman correlation assesses monotonic relationships. Here is a list of correlations within each attribute:
- Diversity
  - Number of ethnicities vs revenue
  - Ethnicity score vs revenue where $ethnicity\ score = \frac{number\ of\ ethnicities}{number\ of\ actors}$
  - Number of female actors vs revenue
  - Fraction of female actors vs revenue
- Runtime
  - Runtime vs revenue
- Plot Summary
  - Positive word proportion vs revenue
  - Negative word proportion vs revenue
  - Violent word proportion vs revenue

### Linear Regression
We performed linear regression to see the correlation between various attributes and revenue especially in the `cast` section. The higher the R-squared value, the better the dependent variable (revenue) is explained by an independent variable in a regression model. We included actors as (categorical) predictors and other relevant variables (budget, genre, release_date and more) which could act as confounders (addressed later) and we extracted the actors that resulted in the highest coefficients, but only for those that had p-value < 0.05. 

### Independent t-test
When investigating each attribute, we divide the dataset into two groups to determine whether there is a statistically significant difference between the means in two unrelated groups. We then simulated the t-test 10 000 times to calculate the statistical power and we use bootstrap with 10 000 draws to compute the 95% CI. Here is a list of t-tests we perform within each attribute:
- Diversity
  - movies with the majority of male actors & movies with the majority of female actors
  - movies with higher ethnicity score (> 0.5) & movies with lower ethnicity score (<= 0.5) 
- Runtime
  - movies with runtime <=80min & movies with runtime >80min
  - runtime of blockbuster (revenue >= $400 million) & runtime of non-blockbuster movies
- Plot Summary
  - movies with more positive plot & movies with more negative plot
  - proportion of positive words in blockbuster plots & proportion of positive words in non-blockbuster plots
  - proportion of negative words in blockbuster plots & proportion of negative words in non-blockbuster plots
  - proportion of violent words in blockbuster plots & proportion of violent words in non-blockbuster plots
  
  
 
  

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
