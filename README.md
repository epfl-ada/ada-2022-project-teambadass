# The Recipe For A Movie Success 🎬
## Abstract
The global film industry is a [`$`100 billion worth industry](https://en.wikipedia.org/wiki/Film_industry). There is a vast potential to earn money, and the producers are willing to sacrifice considerable costs to become a movie success. `Pirates of the Caribbean: On Stranger Tides,` the most expensive film, cost [`$`379 million](https://en.wikipedia.org/wiki/List_of_most_expensive_films). With such an amount at your disposal, you may wonder how you should spend the money. Should you use them to get one of the biggest movie stars in your cast? For many, this may be tempting. One of the most famous actors, `Tom Cruise,` was rewarded [`$`100,000,000](https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors) for his performance in `Top Gun: Maverick.` But was it worth it? Or could the money be better spent? The [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) contains data on the revenue of  8 401 movies. We will analyze this data to create a recipe for a successful movie.

## Research Questions 🔎
In our analysis, we define the success of a movie in terms of box office revenue. To create a recipe for the production of a successful film, we have limited ourselves to five main research questions:

1. Does the movie `release date` have a significant impact on the success of a film, and if so, what is the optimal `release date` concerning the time of the year? Subsequently, the question arises whether this result differs for different `genres.`
2. How do the `gender` ratio and the fraction of `ethnicities` in the cast affect the success of a movie?
3. Do certain `actors` have a significant positive or negative impact on the success of a movie?
4. Is the `length` of a movie related to its success, and if so, in what way?
5. Is the use of `negatively` connoted words, `positively` connoted words, and words related to `violence` in the movie plot associated with the success of the movie?


## Additional Datasets 📈
- [**Budget**](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv) - a dataset containing budget of movies. Budget is essential to reduce the risk of confounding variables when analyzing the relationship between our variables of interest and the `box office revenue.` We will merge this dataset with [**movie.metadata.csv**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link) by combining `movie name,` `release year` and `runtime` to create a unique key for each movie.  
- [**World Bank CPI**](https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG?end=2012&start=1990&view=chart) - a dataset containing country names and inflation data will be used to adjust `budget` and `box office revenue` of the movies. We use the Consumer Price Index (CPI) of the United States to adjust for inflation. CPI is the most widely used measure of inflation, and we use the U.S. as a baseline because both budget and box office revenue are stated in USD. By adjusting for inflation, we can measure financial success in constant dollars, which allows us to compare movies from different years.
- [**IMDB Movies**](https://www.imdb.com/interfaces/) - In addition to defining a movie successful in financial terms, we want to make the definition more diverse by measuring success in terms of ratings. We have extracted two datasets from IMDb - one for making the merge with our movie data possible (`movie name,` `release year,` and `runtime`) and one for extracting the `average rating` and `number of votes` received.
- [**Vocabularies**](https://drive.google.com/drive/folders/1-KcpE8cju60CcNXWc_gPZ6x3V8r7T5eH?usp=share_link) ([**Positive**](https://ptrckprry.com/course/ssd/data/positive-words.txt), [**Negative**](https://ptrckprry.com/course/ssd/data/negative-words.txt), and [**Violence**](https://myvocabulary.com/word-list/violence-vocabulary/)) - We analyze the plot summaries in [**movie.metadata.csv**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link) from three sentiments: `positive,` `negative` and `violent` words and analyze if their proportion in the plot summaries affects `revenue.` 


## Methods 🔤

### T-tests
We use t-tests to determine if there is a significant difference between the groups' means (`revenue`). We simulate the t-tests 10 000 times to calculate the statistical power, and we use bootstrap with 10 000 draws to compute the 95% CI. We have been able to use t-tests without normality because of the central limit theorem. 

### Linear Regression
We performed linear regression with ordinary least squares (OLS) to see the correlation between various attributes and `revenue.` In our initial analysis, we were particularly interested in R-squared to see how our models explain the revenue made.

### Paired Matching
We used paired matching to check for causlity in observed correlations. To match the two groups we standardized the continuous variables, calculated propensity scores and match based on genre and propensity score with a threshold of >0.95.

### Network Analysis
We used network analysis to deepen our understanding and visualize the patterns that exist with respect to actors and the movies they starred in. To gain more insight we use the Louvain method to get best partition of communities in our network, analyse the effect of casting actors belonging to the same community vs. when they are from different communities and use degree centrality to measure the importance of a node in our network.



We describe our choice of methods using our research questions as a baseline. Further details on the steps we describe can be found in [**project_milestone_3.ipynb**](https://github.com/epfl-ada/ada-2022-project-teambadass) with the same structure as the following:

### Step 1: General Pre-Processing
- [**Movie Metadata**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link)
  - We are looking for a recipe to maximize the movie box office revenue. We have therefore removed all movies without `movie_box_office_revenue.`
  -  We adjust the `budget` and `box_office_revenue` for inflation as described in [**Additional datasets**](https://github.com/epfl-ada/ada-2022-project-teambadass/blob/main/README.md). For the project's current stage, we decided to analyze movies back to 1960, which is the first year we have data for inflation. 
- [**Character Metadata**](https://drive.google.com/file/d/1b3_Jn3bBJl6prrtPagU-Yol-ijFMod2u/view?usp=share_link)
  - We removed characters without `freebase_actor_ID.`
  - We merged [**character.metadata.tsv**](https://drive.google.com/file/d/1b3_Jn3bBJl6prrtPagU-Yol-ijFMod2u/view?usp=share_link) with [**movie.metadata.tsv**](https://drive.google.com/file/d/18ZLIKZsH41qls54Gy1qSYW1xtovf9Ke9/view?usp=share_link) on `wikipedia_movie_ID` to be able to explore how actors affect movie revenue.

### Step 2: Release Date
We performed ANOVA testing to determine if there are differences in revenue mean for the movies released in different months. We then conducted 12 t-tests, with one month as one group and the rest as the other group. We repeated this analysis for the 10 most common genres.

### Step 3: Diversity
We used $ethnicity\ score = \frac{number\ of\ ethnicities}{number\ of\ actors}$ and $female\ score = \frac{number\ of\ females}{number\ of\ actors}$ to measure the effect of diversity on revenue made. We used a threshold with $ethnicity\ score = 0.5$ and $female\ score = 0.5$ to create splits of the dataframe and then performed t-tests on the pairwise groups. For more insight we extended our analysis by a range of thresholds and calculated the confidence intervals. Additionally, we performed paired matching to control the effects of confounding variables and estimate causation effects.

### Step 4: Cast
We used One-Hot Encoding of the actors by creating a dummy variable for each actor. We created a new variable for each actor, so we had to experiment with different thresholds to avoid excessively large DataFrames. The threshold corresponds to how many movies the actor has played.
The DataFrame was then used in a linear regression model using the actors as categorical predictors. For more insights in potential patterns we used a network analysis, in which we modeled the actors as nodes and edges as indicators for movies two actors starred in together. We used the Louvain method to extract communities of actors and then analysed if movies, which have a majority of actors from one community or contain more than half of one community, have a higher revenue by using regression.

### Step 5: Runtime
We used runtime and box office revenue to split the DataFrames into pairwise groups on which we performed t-tests. 

### Step 6: Plot Summary
We calculate the proportion of words with `positive` / `negative` / `violent` connotations out of all words in the movie summary. We used t-tests and linear regression to measure the effect of certain terms used to describe the movie.


## Proposed timeline ⏳
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

## Organization within the team 👨‍👩‍👧‍👧
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
    <td class="tg-0lax">Create meaningful visualizations<br><br>Continue exploring the dataset<br><br>Working on the web interface</td>
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
