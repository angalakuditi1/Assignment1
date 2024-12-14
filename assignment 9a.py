#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install --upgrade webdriver-manager


# In[7]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/@PW-Foundation/videos")


# In[9]:


links = driver.find_elements(By.TAG_NAME,"a")
urls = []
for link in links:
    new = link.get_attribute("href")
    urls.append(new)


# In[25]:


first5 = []
for url in urls[11:18]:
    if url == None:
        continue
    else:
        first5.append(url)


# In[27]:


print(first5)


# In[33]:


ervice = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/@PW-Foundation/videos")


# In[40]:


#Q2. Write a python program to extract the URL of the video thumbnails of the first five videos.

thn= driver.find_elements(By.TAG_NAME,"img")
thumbnails = []
for i in thn:
    ths = i.get_attribute("src")
    thumbnails.append(ths)


# In[39]:


thumb_links = []
for thumb in thumbnails[2:8]:
    if thumb == None:
        continue
    else:
        thumb_links.append(thumb)

thumb_links


# In[68]:


#Q3. Write a python program to extract the title of the first five videos.

ervice = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/@PW-Foundation/videos")

ti = driver.find_elements(By.ID, "video-title")


# In[71]:


titl = [element.text for element in ti]
print(titl[0:6])


# In[105]:


#Q4. Write a python program to extract the number of views of the first five videos.


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/@PW-Foundation/videos")

views = driver.find_elements(By.TAG_NAME,"span")


# In[113]:


vw = []
for i in views:
    if str("views") in i.text:
        vw.append(i.text)


# In[115]:


vw[0:6]


# In[203]:


#Q5. Write a python program to extract the time of posting of video for the first five videos.

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.youtube.com/@PW-Foundation/videos")

times = driver.find_elements(By.TAG_NAME,"span")
video_times = []
for i in times[24:]:
    if str("day") in i.text:
        video_times.append(i.text)
print(video_times)


# In[205]:


video_times[0:5]


# In[ ]:




