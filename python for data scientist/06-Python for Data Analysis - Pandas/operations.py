
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[444,555,666,444],
                   'col3':['abc','def','ghi','xyz']})


# In[5]:


df.head()


# In[6]:


df['col2'].unique()


# In[7]:


len(df['col2'].unique())


# In[8]:


df['col2'].nunique()


# In[9]:


df['col2'].value_counts()


# In[12]:


def times(x):
    return x*2


# In[13]:


df['col1'].apply(times)


# In[14]:


df['col1']


# In[15]:


df['col3'].apply(len)


# In[16]:


df['col2'].apply(lambda x: x*2)


# In[17]:


df.drop('col1',axis=1)


# In[26]:


df.columns


# In[22]:


df.index


# In[32]:


df.sort_values('col2')


# In[33]:


df.sort_values(by='col2')


# In[35]:


df.isnull()


# In[36]:


df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo","bar", "bar", "bar", "bar"],
                    "B": ["one", "one", "one", "two", "two","one", "one", "two", "two"],
                    "C": ["small", "large", "large", "small","small", "large", "small", "small","large"],
                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7]})
df


# In[38]:


table = pd.pivot_table(df, values='D', index=['A', 'B'],columns=['C'])


# In[39]:


table

