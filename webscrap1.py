#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E550&maxPrice=600&includeLetAgreed=false")

c=r.content

soup=BeautifulSoup(c, "html.parser")

all=soup.find_all("div", {"class":"propertyCard"})

all[2].find_all("span", {"class":"propertyCard-priceValue"})[0].text


# In[73]:


lista=[]
baseurl="https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E550&maxPrice=600&index=0&includeLetAgreed=false"
for page in range(0,580,24):
    #print(baseurl.replace("index=0","index="+str(page)))
    r=requests.get(baseurl.replace("index=0","index="+str(page)))
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    all=soup.find_all("div", {"class":"propertyCard"})
    all[2].find_all("span", {"class":"propertyCard-priceValue"})[0].text
    for item in all:
        data_dict={}

        data_dict["price"]=item.find("span", {"class":"propertyCard-priceValue"}).text
        data_dict["address"]=item.find("span", {"data-bind":"text: displayAddress"}).text

        lista.append(data_dict)


# In[74]:


len(lista)


# In[75]:


import pandas

dataframe=pandas.DataFrame(lista)

dataframe.to_csv("rightmove_glasgow.csv")

