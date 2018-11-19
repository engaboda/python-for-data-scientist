
# coding: utf-8

# In[1]:


import numpy as np


# In[4]:


arr = np.arange(0,11)


# In[5]:


arr


# In[6]:


arr[4]


# In[7]:


arr[1:5]#execlude the last element


# In[8]:


arr[1:]


# In[12]:


arr[0:11]


# In[13]:


arr[0:2]=100#to update a collection of indexinf at the same time


# In[15]:


arr= np.arange(0,11)


# In[16]:


slice_of_array = arr[0:5]


# In[18]:


slice_of_array[0:]=100


# In[20]:


slice_of_array


# In[21]:


arr


# to avoid this issue we can do copy of array using (arr.copy())
# numpy using this technique to avoid memory leak

# In[22]:


slice_of_array=arr[0:5].copy()


# In[24]:


slice_of_array[0:]=1000


# In[25]:


arr


# #-----------------------------------------------------

# In[26]:


arr_2d=np.array([[1,2,3],[11,22,33],[111,222,333]])


# In[27]:


arr_2d


# In[28]:


arr_2d[1][1]


# In[29]:


arr_2d[1,1]#recomanded to use it


# In[30]:


arr_2d[:2,1:]#


# In[31]:


arr_2d[:2]


# In[32]:


arr_2d[1:,:]


# In[37]:


bool_arr = arr_2d > 10 #this will return bool array


# In[38]:


bool_arr


# In[36]:


arr_2d[bool_arr]#this will return the true value


# In[39]:


arr_2d[arr_2d>10]


# exercies

# In[40]:


exer_arr = np.arange(60).reshape(6,10)


# In[41]:


exer_arr


# In[42]:


exer_arr[3:,1:]


# In[44]:


exer_arr[1:3,3:5]

