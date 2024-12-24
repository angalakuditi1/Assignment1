#!/usr/bin/env python
# coding: utf-8

# Q1: What is Matplotlib? Why is it used? Name five plots that can be plotted using the Pyplot module of
# Matplotlib.

# Matplotlib is a popular Python library used for data visualization. It provides tools to create static, interactive, and animated visualizations in Python. Its flexibility and wide range of features make it a preferred choice for creating high-quality graphs and plots.it is mainly used to creaate the visualization and to analyze the data using the there are many plots that can be used creating this
# scatterplot
# bargraph
# histograph
# pie chart
# line graph

# Q2: What is a scatter plot? Use the following code to generate data for x and y. Using this generated data
# plot a scatter plot.
# import numpy as np
# np.random.seed(3)
# x = 3 + np.random.normal(0, 2, 50)
# y = 3 + np.random.normal(0, 2, len(x))
# Note: Also add title, xlabel, and ylabel to the plot.

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# A scatterplot is a type of data visualization used to represent the relationship between two variables. Each point in the scatterplot represents a single observation in the dataset, with its position determined by the values of the two variables.

# In[10]:


import matplotlib.pyplot as plt
np.random.seed(3)
plt.title("this is my work")
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
plt.xlabel("this is my x axis")
plt.ylabel("this is my y axis")
plt.scatter(x,y)


# Q3: Why is the subplot() function used? Draw four line plots using the subplot() function.
# Use the following data:
# import numpy as np
# For line 1: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([0, 100, 200, 300, 400, 500])
# For line 2: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([50, 20, 40, 20, 60, 70])
# For line 3: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([10, 20, 30, 40, 50, 60])
# For line 4: x = np.array([0, 1, 2, 3, 4, 5]) and y = np.array([200, 350, 250, 550, 450, 150])

# In[19]:


import numpy as np
import matplotlib.pyplot as plt


x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

plt.subplot(3, 3, 2)
plt.plot(x1, y1)
plt.title('Line Plot 1')

plt.subplot(3, 3, 1)
plt.plot(x2, y2)
plt.title('Line Plot 2')

plt.subplot(3, 3, 3)
plt.plot(x3, y3)
plt.title('Line Plot 3')

plt.subplot(3, 3, 4)
plt.plot(x4, y4)
plt.title('Line Plot 4')

plt.tight_layout()

plt.show()


# Q4: What is a bar plot? Why is it used? Using the following data plot a bar plot and a horizontal bar plot.
# import numpy as np
# company = np.array(["Apple", "Microsoft", "Google", "AMD"])
# profit = np.array([3000, 8000, 1000, 10000])

# In[30]:


plt.title("this is graphs")
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.xlabel("the companies")
plt.ylabel("the profit")
plt.bar(company,profit)


# In[28]:


plt.title("my graph")
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.xlabel("the profit")
plt.ylabel("the companies")
plt.barh(company,profit)


# Q5: What is a box plot? Why is it used? Using the following data plot a box plot.
# box1 = np.random.normal(100, 10, 200)
# box2 = np.random.normal(90, 20, 200)

# In[34]:


box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
plt.boxplot(box2)


# In[33]:


box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
plt.boxplot(box1)


# In[ ]:




