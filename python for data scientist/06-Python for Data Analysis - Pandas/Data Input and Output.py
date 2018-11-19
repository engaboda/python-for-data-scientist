
# coding: utf-8

# *CSV
# *HTML
# *SQL
# *EXCEL

# In[2]:


import numpy as np
import pandas as pd


# In[7]:


df = pd.read_excel("Excel_Sample.xlsx")


# In[10]:


df.to_csv("My_output",index=False)#use index=False to not save index as culumn


# In[11]:


pd.read_csv("My_output")


# In[17]:


data = pd.read_html("https://www.fdic.gov/bank/individual/failed/banklist.html")


# In[23]:


data[0].head()


# In[24]:


data[0]


# In[25]:


from sqlalchemy import create_engine


# In[27]:


engin = create_engine("sqlite:///:memory:")


# In[28]:


df.to_sql("my_table",engin)


# In[30]:


sqldf = pd.read_sql("my_table" , engin)


# In[31]:


sqldf

