
# coding: utf-8

# In[1]:


#main tool while working with pandas


# In[2]:


import numpy as np


# In[6]:


import pandas as pd


# In[7]:


from numpy.random import randn


# In[21]:


np.random.seed(0)#that make sure we can get the same random number every time
#makes the random numbers predictable


# In[40]:


np.random.seed(2);np.random.rand(4)#With the seed reset (every time),
#the same set of numbers will appear every time.


# In[78]:


df = pd.DataFrame(randn(5,4), ['A','B','C','D','E'],['Ser1','Ser2','Ser3','Ser4'])


# In[50]:


df#this contain a banch of series sharing the same index


# In[51]:


df['Ser1']


# In[53]:


type(df['Ser1'])


# In[54]:


type(df)


# In[55]:


df.Ser1#not recommanded


# In[56]:


df[['Ser1','Ser2']]# to get a two column pass the name of it as list


# In[57]:


type(df[['Ser1','Ser2']])


# In[59]:


#df['New'] #this will raise KeyError like dict


# In[75]:


df['New']=df['Ser1']+df['Ser2']


# In[62]:


df


# In[64]:


df.drop('New',axis=1)# to remove column axis=1 column and axis=0 for rows


# In[65]:


df#still not delete because we miss using inplace=True to delete it and pandas use it to not loss data


# In[67]:


df.drop('New',axis=1 ,inplace=True)


# In[68]:


df# now it deleted


# In[69]:


df.drop('E')#we not use axis becuase it default for 0 and this not delete data as real 


# In[77]:


df


# In[71]:


df.drop('E',axis=0,inplace=True)


# In[79]:


df.shape


# In[80]:


df.loc['A']# it return series sow column and rows are series and remember to use [] not() :))


# In[81]:


df.iloc[0]#to locate using index


# In[82]:


df


# In[83]:


df.loc['A','Ser1']


# In[85]:


df.loc[['A'],['Ser1','Ser2']]


# In[88]:


df < 0


# In[90]:


df[df > 0]


# In[91]:


df['Ser1']>0


# In[92]:


df['Ser1']


# In[93]:


df[df['Ser1']>0]#this will remove all rows that less than zeros and will not back with Nan


# In[94]:


df


# In[96]:


df[df['Ser4']<0]


# In[99]:


df[df['Ser1']>0]['Ser2']


# In[103]:


df[df['Ser1']>0]


# In[104]:


df['Ser1']


# In[105]:


df


# In[106]:


df[(df['Ser1']>0) and (df['Ser2']>0)]# will raise error (The truth value of a Series is ambiguous)
#and the right way is that we use &


# In[108]:


df[(df['Ser1']>0) & (df['Ser3']>0)]


# In[109]:


df


# In[110]:


df[(df['Ser1']>0) | (df['Ser3']>0)]


# In[111]:


df.reset_index()#to reset index to default like 0 , 1 ,0 to run it use inplace=True


# In[112]:


newind = 'ab ah be da mo'.split()


# In[113]:


df['names']=newind


# In[114]:


df


# In[125]:


df.set_index('names').loc['ab']


# In[126]:


df.set_index('names')

