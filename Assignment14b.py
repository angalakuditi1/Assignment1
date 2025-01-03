#!/usr/bin/env python
# coding: utf-8

# Q1. List any five functions of the pandas library with execution.

# In[1]:


import pandas as pd


# In[2]:


fp = pd.read_csv("titanic passenger list.csv")


# In[4]:


fp.describe()


# In[5]:


fp.head()


# In[6]:


fp.tail()


# In[11]:


fp.groupby('survived')['fare'].sum()


# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

# In[15]:


data = {"A": [1,2,4,5],
        "B": [3,4,5,2],
        "C": [23,45,32,21],
       }


# In[16]:


data


# In[21]:


nw = pd.DataFrame(data)


# In[22]:


nw


# In[27]:


nw.index = range(1,8,2)


# In[28]:


nw.index


# In[29]:


nw


# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.

# In[30]:


data = {'state':("ap","mp","rajasthan","telangana","tamilnadu"),
        'values':(221,443,554,544,322),
       }


# In[33]:


nw = pd.DataFrame(data)
news = nw['values']


# In[34]:


for new in news:
    print(news[0:3].sum())
    break


# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.

# In[36]:


data = {'x':[1,2,3,4,5],
        'text':['raju','ramu','raghu','rasi','ranjan'],
}


# In[39]:


nw = pd.DataFrame(data)
words = nw['text']
nw['word_count'] = ([len(word) for word in words])


# In[40]:


nw


# Q5. How are DataFrame.size() and DataFrame.shape() different?

# DataFrame.size: Returns the total number of elements in the DataFrame (rows × columns). Output: a single integer.
# 
# DataFrame.shape: Returns the dimensions of the DataFrame as a tuple (rows, columns). Output: a tuple.
# 

# In[41]:


#DataFrame.shape
nw.shape


# #DataFrame.size
# nw.size

# Q6. Which function of pandas do we use to read an excel file?
We use pd.read_excel("text.xlsx") to read a file
# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.

# In[108]:


new = {'x':[1,2,3,4,5],
        'Emails':['raju@gmail.com','ramu@gmail.com','raghu@gmail.com','rasi@gmail.com','ranjan@gmail.com'],
}


# In[119]:


words = pd.DataFrame(new)
news = words['Emails']


# In[122]:


words["username"] = [new.split("@")[0] for new in news]


# In[123]:


words


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.
# For example, if df contains the following values:
# A B C
# 0 3 5 1
# 1 8 2 7
# 2 6 9 4
# 3 2 3 5
# 4 9 1 2
# 
# Your function should select the following rows: A B C
# 1 8 2 7
# 4 9 1 2
# The function should return a new DataFrame that contains only the selected rows.

# In[163]:


def filter_dataframe(df):
    filtered_df = df[(df['A'] > 5) & (df['B'] < 10)]
    return filtered_df


# In[164]:


data = { 'A':[3,8,6,2,9],
         'B':[5,2,9,3,1],
         'C':[1,7,4,5,2],
    
}


# In[165]:


df = pd.DataFrame(data)
result = filter_dataframe(df)
print(result)


# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.

# In[166]:


data = {'state':("ap","mp","rajasthan","telangana","tamilnadu"),
        'values':(221,443,554,544,322),
       }


# In[167]:


rj = pd.DataFrame(data)


# In[169]:


#strandard deviation
rj.std()


# In[170]:


#mean
rj.mean()


# In[172]:


#meadian
rj.median()


# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.

# In[180]:


data = {'dates': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05', '2025-01-06', '2025-01-07', '2025-01-08'],
        'sales':[100, 200, 150, 250, 300, 350, 400, 500],}


df = pd.DataFrame(data)
df['dates'] = pd.to_datetime(df['dates'])
df = df.sort_values(by='dates')
df['moving_avarage'] = df['sales'].rolling(window=7, min_periods=1).mean()


# In[181]:


df

Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
Monday, Tuesday) corresponding to each date in the 'Date' column.
For example, if df contains the following values:
Date
0 2023-01-01
1 2023-01-02
2 2023-01-03
3 2023-01-04
4 2023-01-05
Your function should create the following DataFrame:

Date Weekday
0 2023-01-01 Sunday
1 2023-01-02 Monday
2 2023-01-03 Tuesday
3 2023-01-04 Wednesday
4 2023-01-05 Thursday
The function should return the modified DataFrame.
# In[182]:


data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
       }


# In[184]:


new = pd.DataFrame(data)


# In[185]:


new


# In[188]:


import pandas as pd

def add_weekday_column(df):
    df['Date'] = pd.to_datetime(df['Date'])
    
    df['Weekday'] = df['Date'].dt.day_name()
    
    return df

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
}
df = pd.DataFrame(data)
df = add_weekday_column(df)

print(df)

Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python function to select all rows where the date is between '2023-01-01' and '2023-01-31'.
# In[189]:


import pandas as pd

def filter_date_range(df, start_date, end_date):
    df['Date'] = pd.to_datetime(df['Date'])
    filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    return filtered_df

data = {
    'Date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-01-31'],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

result = filter_date_range(df, '2023-01-01', '2023-01-31')
print(result)


# Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
# be imported?

# The first and foremost necessary library to be imported for using the basic functions of pandas is pandas itself.

# In[ ]:




