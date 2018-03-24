
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import warnings
import json 


# In[19]:


df = pd.read_csv('belly_button_biodiversity_otu_id.csv')
otu_df=df.set_index('otu_id')

otu_df

otu_desc = otu_df["lowest_taxonomic_unit_found"].tolist()


# In[24]:


# json_otu=json.dumps(json.loads(otu_df.to_json(orient='index')), indent=2)

json_otu= otu_df.to_json(orient='index')

# print(json_otu)
      


# In[25]:


df1 = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv')

metadata_df=df1.set_index('SAMPLEID')

metadata_dict = metadata_df.to_dict(orient="index")







# json_metadata=json.dumps(json.loads(metadata_df.to_json(orient='index')), indent=2)

# print(json_metadata)





df2 = pd.read_csv('belly_button_biodiversity_samples.csv')


samples_df=df2.set_index('otu_id')



# json_samples=json.dumps(json.loads(samples_df.to_json(orient='index')), indent=4)

samples_header=list(samples_df.columns.values)


# print(json_samples)


# In[36]:


df3 = pd.read_csv('metadata_columns.csv')

metadata_col_df=df3.set_index('COLUMN')

# metadata_col_df



# In[40]:


json_metadata_col=json.dumps(json.loads(metadata_col_df.to_json(orient='index')), indent=6)

# print(json_metadata_col)

