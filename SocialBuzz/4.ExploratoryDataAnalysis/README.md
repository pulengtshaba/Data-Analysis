# Business Questions

1. What are the top 5 categories for 2020 & 2021?
2. How many unique categories are there?
3. How many reactions are there for most popular categories?
4. What was the month with the most Reactions made?

### Objective

Focus on the analysis of sample datasets with visualizations to understand popularity of different content categories, number of different categories, number of reactions for the most popular category, and the month with the most posts.

### Problem solution approach or Analysis process

These tables below are going to be used for Visualization in the next phase of Data Analysis process. Table3[] == Reactions table merged with Content and ReactionType tables.

- Created a new table(5) with ContentCategory, 2020, 2021, and Total as headers. Used ##SUMIFS(Table3[ReactionScore],Table3[ContentCategory],[@ContentCategory],Table3[Year],Table5[[#Headers],[2020]])## formula & autofill to get the sum of reaction score per category. Used ##SUM(Table5[@[2020]:[2021]])## formula to get the sum of reaction score for 2020 & 2021. [Solution]: Top 5 content categories by reaction score and unique categories questions.

- Created a new table with ContentCategory and Reactions as headers. Used ##COUNTIF(Table3[ContentCategory],[@ContentCategory])## formula and autofill to count number of reactions per top 5 category. [Solution]: Number of reactions for the most popular categories.

- Created a new table with Month, Year, and Reactions as headers. Used ##COUNTIFS(Table3[Month],[@Month],Table3[Year],[@Year])## formula & autofill to count number of reactions for each month of 2020 & 2021. [Solution]: Most reactions made per month.
