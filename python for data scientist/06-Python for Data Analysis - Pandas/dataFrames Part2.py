
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[7]:


from numpy.random import randn


# In[15]:


np.random.seed(101)


# In[16]:


df = pd.DataFrame(randn(5,4) , ['A','B','C','D','E'],['W','X','Y','Z'])


# In[19]:


df


# In[24]:


df >0


# In[25]:


df['W'] >0


# In[26]:


df['W']


# In[29]:


df[df['W']>0]


# In[31]:


df[df['Z']<0]


# In[ ]:


#df.reset_index()
#df.set_index('Column Name')

