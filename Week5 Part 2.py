#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


import arcgis


# In[4]:


from arcgis.gis import GIS


# In[5]:


gis = GIS()


# In[6]:


item = gis.content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
flayer = item.layers[0]
sdf = pd.DataFrame.spatial.from_layer(flayer)
sdf.head()


# In[10]:


df = pd.DataFrame({'age':["AGE_10_14", "AGE_15_19", "AGE_20_24", "AGE_25_34", "AGE_35_44", "AGE_45_54"], 'val':[1000, 2000, 3000, 4000, 5000. 6000]})
ax = df.plot,bar(x='age', y='val', rot=0)


# In[ ]:




