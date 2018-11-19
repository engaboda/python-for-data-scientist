
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[7]:


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
     'Person': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
    'Sales':   [200,120,340,124,243,350],
    }


# In[8]:


df = pd.DataFrame(data)


# In[9]:


df


# In[11]:


bycomp = df.groupby('Company')


# In[12]:


bycomp.mean()


# In[13]:


bycomp.sum()


# In[14]:


bycomp.std()


# In[15]:


bycomp.count()


# In[17]:


bycomp.max()


# In[18]:


bycomp.min()


# In[21]:


df.groupby('Company').describe()


# In[22]:


df.groupby('Company').describe().transpose()


# In[25]:


df.groupby('Company').describe().transpose()['FB']

