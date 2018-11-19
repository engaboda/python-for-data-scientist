
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


d = {'A':[1,2,np.nan],'B':[np.nan,1,np.nan],'C':[1,2,3]}


# In[10]:


df = pd.DataFrame(d)


# In[11]:


df


# In[12]:


df.dropna()# will delete all row that have nan value


# In[13]:


df.dropna(axis=0)#this is default value


# In[14]:


df.dropna(axis=1)


# In[25]:


df.dropna(thresh=2)


# In[26]:


df.fillna(value=0.0)


# In[30]:


df['B'].fillna(df['B'].mean())

