#!/usr/bin/env python
# coding: utf-8

# Q1. What is Web Scraping? Why is it Used? Give three areas where Web Scraping is used to get data.
# 
# Web scraping is the process of extracting data from websites. It involves fetching a web page, parsing its content , and extracting the required information for further processing or storage. This is often done using libraries or tools like BeautifulSoup, Selenium, or Scrapy in Python.Web scraping is used when data is not readily available through APIs or structured formats like CSV or JSON. It enables businesses and individuals to collect data from multiple sources for analysis, research, or other purposes.
# 
# It mainly used in market reserach and analysis about comparision and analysis.
# It is also used sentiment analysis of a certain product and job listings

# Q2. What are the different methods used for Web Scraping?
# 
# There are multiple methods of scrapping
# One can be using the simple copy paste the data from the website through simple mehtods and then on use in excel or sheet wheren in the situation happens with the data usage is very limited and simple one.
# one another way is to use API through the request functions to extract the data but not all website provides the apis
# Thats when we use HTML parsing using the libraries and functions like BeautifulSoup.
# Another method is Browser Automation sing tools to mimic user interactions (e.g., clicking buttons, scrolling) and extract data dynamically loaded by JavaScript,many other various ways 

# Q3. What is Beautiful Soup? Why is it used?
# 
# Beautiful Soup is a Python library used for web scraping. It helps extract and navigate data from HTML and XML documents. It creates a parse tree, making it easy to search, modify, or extract specific elements like tags, attributes, and text.
# 
# with the name the method helps to extract the a structured data rather than too much raw data it makes it look beautifully with proper tags,attributes and everything
# 
# To parse HTML/XML documents and make them readable.
# To extract specific data like titles, links, or tables from a webpage.
# To automate data collection for tasks like scraping product reviews or news articles.

# Q4. Why is flask used in this Web Scraping project?
# 
# Flask is used in a web scraping project to create a simple web application that displays the scraped data in a user-friendly way. It acts as a lightweight framework to handle requests, routes, and render the data on a webpage.

# Q5. Write the names of AWS services used in this project. Also, explain the use of each service.
# 
# AMAZON EC2
# Provides virtual servers to host the web application.So, that we can deploy and run your app here.
# 
# AMAZON SC2
# Used to store static files like images, CSS, JavaScript, and other media for the application.
# 
# AMAZON RDS
# Manages relational databases (e.g., MySQL, PostgreSQL) for storing structured data.
# 

# In[ ]:




