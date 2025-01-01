#!/usr/bin/env python
# coding: utf-8

# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[59]:


import pandas as pd


# In[60]:


x = [4,8,15,16,23,42]


# In[63]:


pd.Series(x)


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

# In[64]:


y = [1,43,5,43,55,33,43,22,33,45]


# In[67]:


pd.Series(y)


# Q3. Create a Pandas DataFrame that contains the following data:
#     
#     Name
# Alice
# Bob
# Claire
# 
# Age
# 25
# 30
# 27
# 
# Gender
# Female
# Male
# Female

# In[70]:


new = pd.read_csv('simple.csv')


# In[71]:


type(new)


# In[72]:


new


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# In Pandas, a DataFrame is a two-dimensional, labeled data structure with columns of potentially different data types, similar to a table in a relational database or a spreadsheet in Excel. It is one of the core data structures in Pandas and is used for organizing and analyzing data.
# 
# A Series, on the other hand, is a one-dimensional labeled array capable of holding any data type. A Series can be thought of as a single column of data, while a DataFrame is a collection of Series arranged as columns.

# In[73]:


new


# In[74]:


type(new)


# In[76]:


now = new['Name']


# In[77]:


type(now)


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# Pandas provides a variety of functions to manipulate data in a DataFrame. Here are some common ones

# Handling Missing Data: You can handle missing values using functions like dropna or fillna.
# 
# Filtering Data: You can filter rows based on specific conditions using functions like loc, iloc
# 
# Sorting Data: You can sort the DataFrame by one or more columns using the sort_values function.
# 
# Aggregation: You can perform aggregate operations on specific columns using functions like mean, sum, min, max, etc.
# 
# Grouping Data: You can group data based on certain criteria and perform aggregate functions on each group using groupby.
# 
# Merging DataFrames: You can combine multiple DataFrames using functions like merge or join.We can perform left,right,outer,inner,cross

# In[80]:


nw = {'a':[3,5,9,None],'b':[4,5,None,4]}


# In[84]:


ne = pd.DataFrame(nw)


# In[85]:


nu = ne.dropna()


# In[86]:


nu


# In[89]:


nv = ne.fillna(3)


# In[90]:


nv


# In[93]:


#filterning data
pf = pd.read_html('https://www.espncricinfo.com/records/trophy/batting-most-runs-innings/world-cup-12')


# In[96]:


pp = pf[0]


# In[97]:


pp.head()


# In[99]:


pp.iloc[1:7]


# In[100]:


pp.loc[1:3]


# In[103]:


pp.loc[2:5,["Player","Runs"]]


# In[106]:


pp.iloc[2:5,[2,4,5,6]]


# In[109]:


#sorting data
pp.sort_values(by="Runs",ascending =False)


# In[110]:


#Aggregration
pp['Runs'].max()


# In[113]:


pp['Runs'].min()


# In[115]:


pp['4s'].sum()


# In[118]:


pp[['4s']].mean()


# In[119]:


pp['Balls'].std()


# In[120]:


#Grouping data
pp


# In[ ]:


group = pp.groupby("Runs")


# In[127]:


print(group['Balls'].mean())


# In[ ]:





# In[128]:


data1 = pd.DataFrame({'key1':[1,2,4,5,6],
                      'key2':[4,5,6,7,8],
                      'key3':[3,4,5,6,6]
})


# In[129]:


data2 = pd.DataFrame({'key1':[1,2,5,6],
                      'key4':[5,5,6,7],
                      'key5':[3,4,5,6]
}
)


# In[130]:


pd.merge(data1,data2)


# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# In Pandas, the following are mutable in nature:
# 
# Series: Mutable, meaning you can change the values of a Series after its creation.
# 
# DataFrame: Mutable, meaning you can add, remove, or modify columns or rows in a DataFrame.
# 
# Panel: A Panel is a three-dimensional data structure in Pandas, which could be thought of as a dictionary of DataFrames. Unlike Series and DataFrame, a Panel is not mutable, meaning you cannot change its elements once it is created.

# Panel: A Panel is a three-dimensional data structure in Pandas, which could be thought of as a dictionary of DataFrames. Unlike Series and DataFrame, a Panel is not mutable, meaning you cannot change its elements once it is created.

# In[ ]:





# In[133]:


import pandas as pd


names = pd.Series(["raghu", "rakesh", "arshad", "vinay"])
ages = pd.Series([20, 21, 19, 22])
marks = pd.Series([85, 90, 78, 88])

student_data = pd.DataFrame({
    "Name": names,
    "Age": ages,
    "Marks": marks
})

print(student_data)


# In[ ]:




