
# coding: utf-8

# In[2]:


my_list = [1,2,3,4,5]


# In[5]:


import numpy as np


# In[6]:


np.array(my_list)


# In[7]:


arr = np.array(my_list)


# In[8]:


arr


# conclusion: so we can cast python list to numpy array
# 

# In[9]:


my_mat = [[1,2,3],[11,22,33],[111,222,333]]


# In[10]:


np.array(my_mat)


# to generate array we can use (np.arange([start,]stop[, stop,],dtype=none)) but remember that stop execulde from array

# In[11]:


np.arange(0,100)


# In[12]:


np.arange(0,20,2)


# to generate array of zeros we use (np.zeros(digits))
# 

# In[13]:


np.zeros(3)


# or we can pass the matrix length to zeros as tuple
# 

# In[15]:


np.zeros((3,3))#(rows,columns)


# In[16]:


np.ones((2,3))#just like zeros  but it generate array of ones


# In[18]:


np.ones((4))


# In[30]:


np.linspace(1,2,7)


# In[31]:


np.eye(4)#id matrix that mean digonal is one and all zeros  and must be squar


# In[46]:


np.random.rand(5)*9#random number from zero to one using unformal distrubution


# In[48]:


np.random.rand(2,3)*9


# In[50]:


np.random.randn(3)*9#return sample of 2 not from normal distrubtion but from stander normal dist around zero


# In[51]:


np.random.randn(2,2)


# In[58]:


np.random.randint(1,30)#return random number between (1,30) and  you can pass third argument to retunr spacific number  


# In[59]:


np.random.randint(1,300,5)


# In[68]:


arr = np.arange(40)


# In[69]:


arr


# In[83]:


randarr = np.random.randint(1,100,10)


# In[84]:


randarr


# In[72]:


arr.reshape(4,10)


# In[85]:


randarr.max()#to get max number in array


# In[86]:


randarr.min()#return the min numer in array


# In[87]:


randarr.argmax()#return the index of max number in array 


# In[88]:


randarr.argmin()#return the index of min number in array


# In[92]:


arr.shape#to get shape of array and shape is attribute s call it without ()


# In[93]:


arr.dtype#to get the data type of array but remember that call it without -> ()


# In[96]:


np.random.randint(3,10,100)

