#!/usr/bin/env python
# coding: utf-8

# In[139]:


import pandas as pd


# In[140]:


csv_path = 'budget_data.csv'

py_bank_df = pd.read_csv(csv_path)

py_bank_df.head()


# In[141]:


months_count = py_bank_df['Date'].count

months_count()


# In[142]:


net_total = py_bank_df["Profit/Losses"].sum()

net_total


# In[ ]:





# In[143]:


py_bank_df["Profit/Losses Diff"] = py_bank_df["Profit/Losses"].diff()

profit_loss_average = py_bank_df["Profit/Losses Diff"].mean()

profit_loss_average


# In[147]:


# I couldn't get these to run.
# greatest_increase = py_bank_df["Profit/Losses Diff"].max()

# greatest_decrease = py_bank_df["Profit/Losses Diff"].max()

# greatest_decrease = py_bank_df["Profit/Losses Diff"].min()

# greatest_increase_row = py_bank_df.loc[py_bank_df["Profit/Losses Diff"] == greatest increase, "Date"]
# greatest_decrease_row = py_bank_df.loc[py_bank_df["Profit/Losses Diff"] == greatest decrease, "Date"]

# greatest_decrease_date_df = greatest_decrease_row.iloc[0]
# greatest_increase_date_df = greatest_increase_row.iloc[0]


# In[148]:


print("Financial Analysis")
print("----------------------")
print(f"Total Months: {months_count}")
print(f"Total Revenue: ${net_total}")
print(f"Average Revenue Change: ${profit_loss_average}")
print(f"Greatest Increase: {greatest_increase_date} ({greatest_increase})")
print(f"Greatest Decrease: {greatest_decrease_date} ({greatest_decrease})")


# In[ ]:





# In[ ]:




