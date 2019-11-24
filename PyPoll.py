#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd


# In[48]:


csv_path = "election_data.csv"


# In[49]:


py_poll_df = pd.read_csv(csv_path)

py_poll_df.head()


# In[50]:


Voter_Count = py_poll_df['Voter ID'].count

Voter_Count()


# In[51]:



no_null_votes_df = py_poll_df.dropna(how='any')

    


# In[52]:


no_null_votes_df.count()


# In[53]:


no_null_votes_df["Candidate"].unique()


# In[57]:


columns = ["Voter ID",
          "County" ,
           "Candidate"]

Candidate_Counts = py_poll_df["Candidate"].value_counts()

Candidate_Counts


# In[58]:


Candidate_Counts_df = pd.DataFrame(Candidate_Counts)
Candidate_Counts_df.head()


# In[61]:


# This was an attempt at figuring %
# Candidate_Counts_df['Candidate'] = Candidate_Counts_df['Candidate'].apply(as_percent)  


# In[67]:


#another failed attempt
Winner = [candidate_count].max


# In[ ]:




