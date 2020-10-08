- [Problem Statement](#Problem-Statement)
- [Summary](#Summary)
- [Next Steps](#Next-Steps)
- [Data Dictionary](#Data-Dictionary)
- [External Resources](#External-Resources)

---

## Problem Statement

The Iowa Neighboring Towns Association of Homes (IOWANTAHOME), a regional realty group, has hired my company to build a model to predict house prices in the town of Ames, Iowa. In the course of surveying home listings, IOWANTAHOME collects 81 data pointes on each residence. 

---

## Summary

My analysis began by examining numerical categories (nb link) a heatmap to evaluate correlation between the numerical features and the target, sale price. I initially chose the top 10 most correlated, and then filtered out 3 that were highly correlated with each other (example: garage area and number of cars that can fit in the garage). As I continued to refine my model, I added correlations above .4, and eventually those above .3 and saw the expected marginal gains at each iteration. This is a heatmap specifically of the aspects I chose to include.


<img src="./notebooks&images/images/image_name.png" width="75%" height="75%">

Note: there are some additional engineered columns, like 'garage' which was a multiple of garage area (square footage) times garage cars (number of cars that fit in the garage). I found this to be a more accurate metric than either of those two individual scores, so I dropped them from my model and used my engineered metric instead.

In a separate notebook (nb link), I evaluated categorical features. After reading through the full data dictionary on kaggle (link), I selected those which appeared most promising and evaluated them one-by-one to see which had clear groupings in relation to sale price. Having checked value counts, pair plots, and other related metrics (depending on what the category was designed to measure), I made the necesary adjustments in my processing algorithm to include the features which displayed obvious patterns correlated to sale price. In most cases this involved grouping the different components of the features that appeared in similar price brackets into a new column in order to reduce my model's total number of columns and eliminate the possibility of mismatch between columns in training and test. Below is an example of neighborhood price sorted by (metric). I found this to be a more reasonable method of sorting neighborhood values as opposed to simple geography as the physical proximity of of one neighborhood to another does not necessarily indicate proximity in pricing.

<img src="./notebooks&images/images/image_name.png" width="75%" height="75%">


My best model came by including the following features - separated by into numerical and categorical:

Numerical:

Categorical:

I also applied a logarithmic transformation to my sale price (y) value and then exponentiated it at the end - this reduced the differences between the outliers at the very top end of sale price so that my model had a more accurate fit. I wrote a function which I used repeatedly as I tried new combinations of features - it takes in three arguments - dataframe name, feature list, categorical feature list - and returns all the relevant metrics related to the quality of the model. Here is a display of the output for my best model:

(best model picture of residuals and related scores)

|                     |           |         |
|:--------------------|:----------|:--------|
| state               | Minnesota | Nevada  |
| avg_participation   | 0.98      | 1.0     |
| avg_composite       | 21.4      | 17.8    |

Whenever I found a model that scored better than it's predecessors, I fed the same information that my make_model() function accepts into another function I wrote called save_test(). This function instantiates the model, prints my R2 score for the model, then loads in the test data, cleans the test data, and shows my the top five rows (head) of my potential submission dataframe. It then accepts an input command - "yes" or "no" and if I like what I see, I can enter "yes" and it will save the model named after the current timestamp, ensuring that I never accidentally overwrite a previously saved model. Here is what that output looked like on my top model:

(best test output)

In conclusion - this model is the best mixture of simplicity and refinement - it strategically includes the numerical and categorical features that correlate best with sale price, while simultaneously excluding extraneous features.

---

### Next Steps

Text

---

### Data Dictionary

|Feature|Type|Dataset|Description|
|---|---|---|---|
|**state**|*string*|act2017(2018,2019)|Regional, municipal subset of the United States of America.| 
|**participation**|*float*|act2017(2018,2019)|Percentage of a state's eligible students that took the ACT in a given year, represented as a decimal out of 1|
|**composite**|*float*|act2017(2018,2019)|The average score across all students who took the ACT in the given year (max possible score 36)|
|**exp_composite**|*float*|act2017df(2018,2019)|The expected average ACT for a given state based on their participation; drawn from linear regression best fit line of participation,composite scatter plot|
|**difference**|*float*|act2017df(2018,2019)|Each states expected composite score (based on linear regression) minus their actual score; may be positive or negative to reflect achievement above or below expected|
|**2017(2018)median_inc**|*float*|act2017df(2018)|Median income for given year based on census.gov website. Not available for 2019.|
|**student_teach_ratio**|*string*|summary_data|Average student to teacher ratio across given state|
|**median_teach_salary**|*int*|summary_data|Median teach salary in given state|
|**per_student_spend**|*int*|summary_data|Average spent on each student in given state|
|**avg_participation**|*float*|summary_data|Three year average of overall participation for given state|
|**avg_composite**|*float*|summary_data|Three year average of overall composite score for given state|
|**avg_exp_composite**|*float*|summary_data|Three year average of expected composite score based on participation for a given state|
|**avg_difference**|*float*|summary_data|Three year average of difference between expected and actual score for given state|
|**avg_median_inc**|*float*|summary_data|Average of 2017 and 2018 median income for given state - 2019 data unavailable|

---

### External Resources

Paste links here