
# coding: utf-8

# In[1]:


#First Main Datatype
#Series can Access using Label


# In[6]:


import numpy as np


# In[7]:


import pandas as pd


# In[21]:


label = ['a','b','c']
my_data=[10,20,30]
arr = np.array(my_data)
d= {'a':10,'b':20,'c':30}


# In[29]:


pd.Series(data=my_data)


# #pd.Series(my_data,label) equal of pd.Series(data=my_data,index=label)

# In[24]:


pd.Series(data=my_data , index=label)#should all of my_data and label are equal in shape of data


# In[28]:


np.shape(d)


# In[30]:


pd.Series(my_data)


# In[31]:


pd.Series(d)# its great thing because it take key from dict and use it as index for values :)


# In[32]:


pd.Series(label)#it deal with almostof any datatype of python


# In[34]:


pd.Series(data=[sum,print,len])


# In[35]:


ser = pd.Series(data=[sum,print,len])


# In[39]:


ser[1]


# In[40]:


ser1 = pd.Series([1,2,3,4],['eg','usa','tr','uae'])


# In[41]:


ser1


# In[54]:


ser2 = pd.Series([1,2,5,6],['eg','usa','c','uae'])


# In[44]:


ser2


# In[52]:


ser2['c']


# In[55]:


ser1+ser2#first will look at index and will add to match each other and if not find will return nan &&
#and integer will converted to float

