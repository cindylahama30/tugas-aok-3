#!/usr/bin/env python
# coding: utf-8

# In[1]:


# masukkan library yang akan kita gunakan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# melakukan pembacaan pada dataset dalam format 
data = pd.read_csv('tugas3.csv')


# In[2]:


data.info()


# In[4]:


#print 10 data pertama
data.head(10)


# In[5]:


# Dimensi data
data.shape


# In[6]:


# Deskripsi data
data.describe()


# In[7]:


data.corr()


# In[8]:


correlations = data.corr(method ="kendall")
correlations


# In[9]:


# correlation map
# higher correlations are brighter
f,ax = plt.subplots(figsize=(20,20))
sns.heatmap(correlations, annot=True, linewidths=.5, fmt='.3f', ax=ax)
plt.show


# In[ ]:




