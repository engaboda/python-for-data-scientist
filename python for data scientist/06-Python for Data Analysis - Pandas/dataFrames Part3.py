
# coding: utf-8

# In[15]:


import numpy as np


# In[16]:


from numpy.random import randn


# In[3]:


import pandas as pd


# In[12]:


#index Level
outside    = ['G1','G1','G1','G2','G2','G2']
inside     =[1,2,3,1,2,3]
hier_index =list(zip(outside,inside))
hier_index =pd.MultiIndex.from_tuples(hier_index)


# In[13]:


hier_index


# In[18]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])


# In[19]:


df


# In[22]:


df.loc['G1'].loc[1]


# In[28]:


df.index.names = ['Group','Num']


# In[29]:


df


# In[30]:


df.index.names


# In[35]:


df.loc['G2']


# In[36]:


df.loc['G2'].loc[2,'B']


# In[37]:


df.xs('G1')


# In[38]:


df


# In[39]:


df.xs(1,level='Num')

