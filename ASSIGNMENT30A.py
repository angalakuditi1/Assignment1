#!/usr/bin/env python
# coding: utf-8

# Q1. What is anomaly detection and what is its purpose?
Anomaly detection is the process of identifying things that don’t follow the normal pattern in data. In simple terms, it’s like spotting a rotten apple in a basket of fresh apples. The main goal is to detect unusual behavior or events that might indicate problems, fraud, or important changes.

For example, if your electricity bill suddenly becomes 5 times higher than usual, anomaly detection would flag it as odd. Businesses use this technique in many areas—banks use it to spot fraud, doctors use it to catch unusual patient symptoms, and factories use it to detect machine failures before they happen.

The purpose is to catch issues early, save money, improve safety, and make better decisions. By detecting these anamolies quickly, companies can prevent bigger problems and respond faster to unexpected situations.
# Q2. What are the key challenges in anomaly detection?
Anomaly detection faces several key challenges. First, anomalies are rare and diverse, making it difficult to define a clear boundary between normal and abnormal behavior. Second, labeled data is often scarce, especially for anomalies, hindering supervised learning. Third, real-world data is noisy and high-dimensional, complicating the identification of subtle outliers. Fourth, anomalies can evolve over time, requiring models that adapt to changing patterns. Fifth, in domains like cybersecurity or finance, false positives can be costly, so high precision is crucial. Additionally, unsupervised methods may detect statistically rare events that are not actually significant anomalies. Finally, scalability is a concern when dealing with large datasets in real-time systems. Addressing these challenges requires a combination of robust algorithms, domain knowledge, and continual model evaluation.
# Q3. How does unsupervised anomaly detection differ from supervised anomaly detection?
Unsupervised anomaly detection and supervised anomaly detection both aim to find unusual or abnormal data, but they differ in how they learn what is "normal."

In supervised anomaly detection, the system is trained using labeled data—examples clearly marked as “normal” or “anomalous.” It learns patterns from this data and can then spot similar anomalies in new data. This is like a teacher showing a student good and bad examples before a test.

In unsupervised anomaly detection, there are no labels. The system has to figure out patterns on its own and decide what looks unusual. It assumes that most data is normal and flags anything that doesn’t fit the usual pattern. This is like a student figuring things out without any guidance.

Unsupervised methods are useful when we don’t have clear examples of anomalies, while supervised methods are more accurate when labeled data is available. Each is useful in different real-world situations.
# Q4. What are the main categories of anomaly detection algorithms?
Anomaly detection algorithms are mainly grouped into three categories: supervised, unsupervised, and semi-supervised.

Supervised methods work like a teacher-student setup. They need labeled examples of both normal and abnormal behavior to learn the difference. These are great if you already know what "wrong" looks like.

Unsupervised methods don’t need labeled data. They look for data points that behave very differently from the rest. Think of it like spotting the one person in a crowd wearing a bright red suit — they just stand out.

Semi-supervised methods are a mix. They learn from lots of normal data and then try to spot anything that doesn’t match that pattern. It’s like learning what usual customer spending looks like and then catching strange transactions.

Each method fits different real-life situations, depending on whether you already know what anomalies look like or not. Choosing the right one depends on your data and the problem you're solving.
# Q5. What are the main assumptions made by distance-based anomaly detection methods?
Distance-based anomaly detection methods assume that normal data points are close to each other, while anomalies (outliers) are far away from other points. In simple terms, think of data points as people at a party. Most people (normal data) are standing in groups chatting (close together), but someone who is standing alone far from everyone else (anomaly) looks suspicious or unusual.

Here are the main assumptions in layman terms:

Closeness means normal: If a data point has many nearby neighbors, it is likely normal.
Isolation means abnormal: If a point is far away from most others, it may be an anomaly.
Distance is meaningful: The space between points can be measured accurately.
Data is evenly distributed: No hidden groups or clusters that might confuse the method.

These assumptions work well in simple datasets but can fail if the data has complex patterns or many dimensions.
# Q6. How does the LOF algorithm compute anomaly scores?
The Local Outlier Factor (LOF) algorithm finds anomalies (outliers) by comparing how isolated a data point is from its neighbors. Imagine you're standing in a crowd. If you're far away from everyone else, and those people are standing close to each other, you're likely an outlier.

LOF checks:

How close each point is to its neighbors (local density).
How your density compares to your neighbors’ density.

If your neighbors are packed tightly together and you're far away, you’re more likely to be an anomaly. It gives each point a score — higher means more likely to be an outlier. A score around 1 means you're normal, and higher than 1 means you're an outlier.
# Q7. What are the key parameters of the Isolation Forest algorithm?
The Isolation Forest algorithm is a machine learning method used to detect anomalies (outliers) in a dataset. It works by creating random "trees" to separate data points and identifies which points are harder to isolate. The key parameters of the Isolation Forest are:

n_estimators: This controls how many trees (models) the algorithm will build. More trees generally improve performance but take longer to compute.

max_samples: It determines the number of data points the algorithm will randomly sample to build each tree. A larger sample size makes the model more accurate but requires more computation.

contamination: This parameter specifies the proportion of outliers in the dataset. It's used to set the threshold for deciding what counts as an anomaly.

random_state: It ensures reproducibility by controlling the randomness in the model-building process.
# Q8. If a data point has only 2 neighbours of the same class within a radius of 0.5, what is its anomaly score using KNN with K=10?
In K-Nearest Neighbors (KNN), we check how similar a data point is to its K closest neighbors. If most neighbors are different, the point is considered unusual or an anomaly. Here, with K = 10, only 2 neighbors are from the same class, meaning 8 are different. We calculate the anomaly score as:

Anomaly Score = 1 − same-class neighbors/𝐾

              = 1 − 2/10 = 0.8
This means the point is 80% different from its neighbors and likely an anomaly. So, the final anomaly score is 0.8.
# Q9. Using the Isolation Forest algorithm with 100 trees and a dataset of 3000 data points, what is the
# anomaly score for a data point that has an average path length of 5.0 compared to the average path
# length of the trees?
The anomaly score in the Isolation Forest algorithm measures how much a data point deviates from normal data. It is calculated using the formula:

Anomaly Score = 2 − 𝐸(ℎ(𝑥))/𝑐(𝑛)
Anomaly Score=  2 − c(n)
E(h(x)) is the average path length of the point, and c(n) is the correction factor that adjusts for dataset size. For a dataset of 3000 points, with an average path length of 5.0, the correction factor 

c(n) is calculated, and the anomaly score is computed. In this case, the anomaly score is approximately 0.796.
# In[ ]:




