#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
tables = pd.read_html( 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')[0]


# In[2]:


tables.head()


# In[3]:


tables['Borough'].replace('Not assigned',np.nan,inplace = True)


# In[5]:


tables.dropna(subset =['Borough'],axis = 0,inplace = True )


# In[13]:


tables.head()


# In[14]:


tables.groupby('Postal Code')


# In[21]:


tables.reset_index(drop = True,inplace = True)
tables[0:12]


# In[22]:


tables.shape


# In[ ]:




