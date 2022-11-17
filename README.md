# The recipe for a movie success 
## Abstract
The global film industry is a [`$`100 billion worth industry](https://en.wikipedia.org/wiki/Film_industry). There is a vast potential to earn money, and the producers are willing to sacrifice considerable costs to become a movie success. `Pirates of the Caribbean: On Stranger Tides,` the most expensive film, cost [`$`379 million](https://en.wikipedia.org/wiki/List_of_most_expensive_films). With such an amount at your disposal, you may wonder what you should spend the money on. Should you use them to get one of the biggest movie stars in your cast? For many, this may be tempting. One of the most famous actors, `Tom Cruise,` was rewarded [`$`100,000,000](https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors) for his performance in `Top Gun: Maverick.` But was it worth it? Or could the money be better spent? The [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) contains data on the revenue of  8 401 movies. We will analyze this data to create a recipe for a successful movie.

## Research Questions (TODO: @anni5701)

## Additional Datasets (TODO: @torkelwestby)
- [**Budget**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv) - a dataset containing budget of movies. Buwdget is essential to reduce the risk of confounding variables when analyzing the relationship between our variables of interest and the box office revenue. 
- [**World Bank CPI**](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2012&start=1990&view=chart) - a dataset containing country names and inflation data will be used to adjust budgets and box office revenues of the movies. We use the Headline Consumer Price Index (CPI) of the United States to adjust for inflation. CPI is the most widely used measure of inflation, and we use the U.S. as a baseline because both budget and revenue are stated in USD in our datasets. By adjusting for inflation, we can measure financial success in constant dollars, which allows us to compare movies from different years. 
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - In addition to defining a movie successful in financial terms, we want to make the definition more diverse by measuring success in terms of ratings received as well. In addition to the movie title used for merging, we only use the average vote and vote count in this dataset. 


## Methods (TODO: @kevinxyc1 & @anni5701)

### Data Preprocessing
- We are looking for a recipe to maximize the movie box office revenue. We have therefore removed all movies without revenue.
- We normalize the revenue by taking account into inflation between 1960 to 2014 so that movies are more comparable.

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
