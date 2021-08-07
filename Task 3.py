#!/usr/bin/env python
# coding: utf-8

# # NAME - SONALI PATIL
# # TASK 3 - Exploratory Data Analysis[EDA] - Retail (Level - Beginner)
# 
# 
# 

# In[51]:


# Import all required labraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotnine import *


# In[2]:


# Load dataset

data=pd.read_csv('D:\\SampleSuperstore.csv')


# In[3]:


data.head() # It will give info abt first 5 row of dataset


# In[4]:


data.tail() # It gives info abt last 5 row of dataset


# In[5]:


data.info() # Returns summary of dataset


# In[6]:


data.describe() # Gives statistical data


# In[7]:


data.shape # info about row and col


# In[8]:


data.columns # col nm


# In[9]:


data.nunique() # cheacking unique values


# # Cleaning the data

# In[10]:


# Cleaning the data

data.isnull().sum()   # cheacking the null values


# # Checking duplicate data

# In[12]:


# Checking for duplicate data .If yes then drop the data
   
data.duplicated().sum()


# In[14]:


# In this 17 duplicate data found then drop those data

data.drop_duplicates()


# # After the dropping data

# In[15]:


# After dropping data

data.head()


# In[16]:


data.tail()


# In[17]:


data.info()


# In[18]:


data.describe()


# In[20]:


# Checking unique value

data.nunique()


# # Dropping irrelevant column

# In[24]:


## Deleting col

col=['Postal Code']
data1=data.drop(columns=col,axis=1)


# # Checking Statistical relation bet. various row and col

# In[25]:


# co-relation between between variables
data1.corr()


# In[26]:


# Covarience of column
data1.cov()


# # After dropping irrelevant column[Postal Code] cheacking info abt  head,tail,info,describe,nunique and null

# In[27]:


data1.head()


# In[28]:


data1.tail()


# In[29]:


data1.info()


# In[30]:


data1.describe()


# In[31]:


data1.isnull().sum()


# In[33]:


data1.nunique()


# # Data Visualization 

# In[56]:


plt.figure(figsize=(16,8))
plt.bar('Sub-Category','Category',data=data1)
plt.title('Category vs Sub-Category')
plt.xlabel('Category')
plt.ylabel('Sub-Category')
plt.xticks(rotation=90)
plt.grid()
plt.show()


# In[42]:


data1.corr()


# In[44]:


data1.hist(bins=50,figsize=(20,16))
plt.show()


# In[46]:


# checking repeatable states

data1['State'].value_counts()


# In[55]:


plt.figure(figsize=(15,10))
sns.countplot(x=data1['State'])
plt.xticks(rotation=90)
plt.title('STATE')
plt.show()


# In[59]:


Profit_plot =(ggplot(data, aes(x='Sub-Category' , y='Profit', fill='Sub-Category'))+ geom_col()+coord_flip()
              + scale_fill_brewer(type='div',palette='Spectral')+ theme_classic()+ggtitle('Pie-Chart'))

display(Profit_plot)


# # Above pie chart show us profit and loss of each and every sub category

# In[60]:


sns.pairplot(data1)


# In[61]:


sns.relplot(x='Category', y='Sub-Category',hue='Ship Mode',data=data1)


# In[63]:


sns.relplot(x='Category', y='Sub-Category',hue='Segment',data=data1)


# # Thank You !!!!!

# In[ ]:




