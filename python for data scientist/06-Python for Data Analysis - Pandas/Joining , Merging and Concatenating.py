
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


df = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3'],
                  } , index=[0,1,2,3])


# In[6]:


df1 = pd.DataFrame({'A':['A00','A10','A20','A30'],
                   'B':['B00','B10','B20','B30'],
                   'C':['C00','C10','C20','C30'],
                   'D':['D00','D10','D20','D30'],
                  } , index=[4,5,6,7])


# In[7]:


df1


# In[8]:


df2 = pd.DataFrame({'A':['A000','A100','A200','A300'],
                   'B':['B000','B100','B200','B300'],
                   'C':['C000','C100','C200','C300'],
                   'D':['D000','D100','D200','D300'],
                  } , index=[8,9,10,11])


# In[9]:


df2


# In[10]:


#Concatination basicully  glues together DataFrame Keep in mind That
#dimensions should match along the axis you are concatinating on You can use (pd.concat())


# In[11]:


pd.concat([df,df1,df2])


# In[13]:


pd.concat([df,df1,df2],axis=1)


# In[15]:


left = pd.DataFrame({'Key':['k0','k1','k2','k3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3'],
                    } )


# In[16]:


left


# In[17]:


right = pd.DataFrame({'Key':['k0','k1','k2','k3'],
                     'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3'],
                    } )


# In[18]:


right


# In[19]:


pd.merge(left,right,how='inner',on='Key')


# In[23]:


left = pd.DataFrame({'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3'],
                    },index=['k0','k1','k2','k3'] )

right = pd.DataFrame({'C':['C0','C1','C2','C3'],
                     'D':['D0','D1','D2','D3'],
                    },index=['k0','k1','k2','k3'] )


# In[24]:


left.join(right)

