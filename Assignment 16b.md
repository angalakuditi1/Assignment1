Q1. What are the three measures of central tendency?

The three measures of central tendency are mean, median, and mode

Mean: The arithmetic average, calculated by dividing the sum of all data points by the total number of points. It is sensitive to extreme values (outliers).
Formula:

Median: The middle value when data is ordered. For an odd number of values, it's the middle one; for an even number, it's the average of the two middle values. It’s less affected by outliers.

Mode: The most frequently occurring value(s) in a dataset. A dataset can have one mode, multiple modes, or no mode if all values occur equally often.

These measures summarize data, giving insights into its central point. Each is useful depending on the type and distribution of the dataset.

Q2. What is the difference between the mean, median, and mode? How are they used to measure the
central tendency of a dataset?


Mean: The average of all data points, calculated by dividing the sum of the values by the number of observations. It is sensitive to extreme values (outliers), which can skew the result. For example, a dataset of incomes may have a high mean due to a few very wealthy individuals.

Median: The middle value when the data is ordered. If the dataset has an even number of observations, it is the average of the two middle values. The median is robust to outliers and represents the central point of the dataset.

Mode: The most frequently occurring value(s) in the dataset. It is useful for categorical or discrete data.

Together, these measures help describe the data distribution, identify trends, and make informed decisions in statistics and data analysis.

Q3. Measure the three measures of central tendency for the given height data:
[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

Mean = 178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5/16 = 169.39375
Median = 172.5, 175, 175, 176, 176.2, 176.5, 177, 177, 177, 178, 178, 178, 178.2, 178.9, 179, 180,Median= 177+177/2,177
Mode = 178

Q4. Find the standard deviation for the given data:
[178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]

import numpy as np
lst = [178,177,176,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]


```python
np.std(lst)
```




    1.7885814036548633



Q5. How are measures of dispersion such as range, variance, and standard deviation used to describe
the spread of a dataset? Provide an example.

Measures of dispersion describe the spread or variability of a dataset, providing insights into how data points differ from each other and the central value.

1. Range: The simplest measure, calculated as the difference between the maximum and minimum values. It shows the overall spread but is sensitive to outliers.
Example: If scores in a test are 60, 70, 80, 90, and 100, the range is. range = 100-60 = 40 

2. Variance: Measures the average squared deviations from the mean, offering insight into the dataset's variability. A high variance indicates greater spread.

3. Standard Deviation (SD): The square root of variance, SD provides the average deviation from the mean in the same units as the data. It is more interpretable than variance.
Example: For the scores above, if the mean is 80, a standard deviation of 10 means most scores fall within 80±10

These measures help in comparing datasets and understanding data consistency.


Q6. What is a Venn diagram?

A Venn diagram is a visual representation used to show relationships between different sets or groups. It consists of overlapping circles, where each circle represents a set. The overlapping regions indicate elements shared between the sets, while non-overlapping parts represent unique elements. Venn diagrams are commonly used in mathematics, logic, statistics, and data science to illustrate intersections, unions, and differences between sets. For example, they can demonstrate common interests between groups or shared characteristics in datasets. Easy to understand and interpret, Venn diagrams provide a clear, intuitive way to analyze and compare relationships between multiple sets or categories.

Q7. For the two given sets A = (2,3,4,5,6,7) & B = (0,2,6,8,10). Find:
(i)  A B
(ii) A ⋃ B

(i) (2,6)
(ii) (2,3,4,5,6,7,8,10)

Q8. What do you understand about skewness in data?

Skewness in data refers to the asymmetry in the distribution of values. If the data is symmetrically distributed around the mean, it has zero skewness. Positive skewness (right-skewed) indicates that the tail on the right side is longer or heavier, with most data
concentrated on the left. Negative skewness (left-skewed) means the tail on the left is longer, with most data concentrated on theright. Skewness helps identify deviations from a normal distribution, affecting statistical analysis and model performance. It is critical in understanding data behavior, summarizing distributions, and deciding transformations or techniques for further analysis.

Q9. If a data is right skewed then what will be the position of median with respect to mean?

it will be mode<median<mean 
In a right-skewed distribution, the mean is greater than the median because the tail of the data stretches to the right due to higher values. The median lies closer to the bulk of the data, while the mean shifts rightward due to the influence of extreme values.

Q10. Explain the difference between covariance and correlation. How are these measures used in
statistical analysis?

Covariance and correlation both measure relationships between variables, but they differ in scale and interpretation. Covariance indicates the direction of the linear relationship between variables (positive or negative), but its value depends on the variables' units, making it hard to compare across datasets. Correlation standardizes covariance, producing a dimensionless value between -1 and 1, where -1 signifies a strong negative, 1 a strong positive, and 0 no linear relationship.

In statistical analysis, covariance is used to assess variable relationships, while correlation quantifies the strength and direction, aiding in regression models, feature selection, and identifying significant patterns in data.

Q11. What is the formula for calculating the sample mean? Provide an example calculation for a
dataset.

nw = [12,11,22,43,42,21,83]
sample mean = x = summetion of xi/n = 234/7
which is 33.42

Q12. For a normal distribution data what is the relationship between its measure of central tendency?

In a normal distribution, the mean, median, and mode are all equal and located at the center of the distribution. This symmetry means that the data is evenly distributed around the central point, with 50% of the data falling on either side. These measures of central tendency align in normal distributions.

Q13. How is covariance different from correlation?

Covariance measures the degree to which two variables change together, but it depends on their units. Correlation, on the other hand, normalizes the covariance, making it unit-independent and providing a value between -1 and 1 to indicate the strength and direction of the relationship between variables.

Q14. How do outliers affect measures of central tendency and dispersion? Provide an example.

Outliers can significantly skew measures of central tendency and dispersion. For example, the mean is sensitive to extreme values, making it higher or lower than the majority of the data. The standard deviation increases, giving a misleading impression of data spread. The median and interquartile range are less affected.


```python

```
