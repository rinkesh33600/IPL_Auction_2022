#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[50]:


ipl=pd.read_csv('F:\Downloads\ipl_2022_data.csv')


# In[51]:


ipl.head()


# In[52]:


ipl.shape


# In[53]:


ipl.info()


# In[54]:


ipl.columns


# In[55]:


ipl.drop('Unnamed: 0',axis=1, inplace=True)


# In[56]:


ipl.head()


# In[57]:


ipl.isnull().sum()


# In[58]:


ipl[ipl['Cost IN $ (000)'].isnull()]


# In[59]:


ipl['COST IN(CR.)'] = ipl['COST IN(CR.)'].fillna(0)
ipl['Cost IN $ (000)'] = ipl['Cost IN $ (000)'].fillna(0)


# In[60]:


ipl.isnull().sum()


# In[61]:


ipl['2021 Squad']=ipl['2021 Squad'].fillna('Not Participated')


# In[62]:


ipl.isnull().sum()


# In[63]:


ipl.info()


# In[64]:


teams=ipl[ipl['COST IN(CR.)']>0]['Team'].unique()
teams


# In[65]:


ipl['status']=ipl['Team'].replace(teams,'sold')


# In[66]:


ipl


# In[67]:


ipl[ipl['Player'].duplicated(keep=False)]


# In[68]:


# How many players have participated in 2022 IPL Auction?

ipl.shape[0]


# In[69]:


# How many types of players have participated? 

types=ipl['TYPE'].value_counts()
types.reset_index()


# In[70]:


plt.pie(types.values, labels=types.index,labeldistance=1.2,autopct='%1.2f%%', shadow=True, startangle=60)
plt.title('Role of Players Participated', fontsize = 15)
plt.plot()


# In[71]:


# Players sold and unsold using a bar graph.

plt.figure(figsize=(10,5))
fig=sns.countplot(ipl['status'],palette=['Orange','Pink'])
plt.xlabel('Sold or Unsold')
plt.ylabel('Number of Players')
plt.title('Sold vs Unsold', fontsize=15)
plt.plot()
for p in fig.patches:
    fig.annotate(format(p.get_height(), '.0f'), (p.get_x() +
    p.get_width()/2., p.get_height()), ha = 'center', va='center', 
    xytext= (0, 4), textcoords='offset points')


# In[72]:


ipl.groupby('status')['Player'].count()


# In[73]:


plt.figure(figsize=(20,10))
fig=sns.countplot(ipl[ipl['Team']!='Unsold']['Team'])
plt.xlabel('Team Names')
plt.ylabel('Number of Players')
plt.title('Players Bought by Each Team', fontsize=12)
plt.xticks(rotation=70)
plt.plot()

for p in fig.patches:
    fig.annotate(format(p.get_height(), '.0f'), (p.get_x() +
    p.get_width()/2., p.get_height()), ha='center', va='center',
    xytext = (0,4), textcoords = 'offset points')


# In[74]:


ipl['retention'] = ipl['Base Price']


# In[75]:


ipl.head()


# In[76]:


ipl['retention'].replace(['2 Cr', '40 Lakh', '20 Lakh', '1 Cr', '75 Lakh', '50 Lakh', '30 Lakh', '1.5 Cr'],'From Auction', inplace=True)


# In[77]:


ipl.head()


# In[78]:


# Treating Base Price

ipl['Base Price'].replace('Draft Pick',0, inplace = True)


# In[79]:


ipl.head()


# In[80]:


ipl['base_price_unit'] = ipl['Base Price'].apply(lambda x: str(x).split(' ')[-1])
ipl['base_price'] = ipl['Base Price'].apply(lambda x: str(x).split(' ')[0])


# In[81]:


ipl['base_price'].replace('Retained',0,inplace=True)


# In[82]:


ipl.head()


# In[83]:


# Total players retained and bought
ipl.groupby(['Team','retention'])['retention'].count()[:-1]


# In[84]:


plt.figure(figsize=(20,10))
fig=sns.countplot(ipl[ipl['Team']!='Unsold']['Team'],hue=ipl['TYPE'])
plt.title('Players in Each Team')
plt.xlabel('Team Names')
plt.ylabel('Number of Player')
plt.xticks(rotation=50)


# In[85]:


# Highest amount spent on a single player by each team
ipl[ipl['retention']=='From Auction'].groupby(['Team'])['COST IN(CR.)'].max()[:-1].sort_values(ascending = False)


# In[86]:


#Player retained at maximum price
ipl[ipl['retention']=='Retained'].sort_values(by = 'COST IN(CR.)',ascending = False).head(1)


# In[87]:


# Top 5 Bowlers

ipl[(ipl['retention']=='From Auction') & (ipl['TYPE']=='BOWLER')].sort_values(by='COST IN(CR.)',ascending = False).head(5)


# In[88]:


# top 5 Batsman
ipl[(ipl['retention']=='From Auction') & (ipl['TYPE']=='BATTER')].sort_values(by='COST IN(CR.)',ascending = False).head(5)


# In[89]:


# TOP 5 allrounder
ipl[(ipl['retention']=='From Auction') & (ipl['TYPE']=='ALL-ROUNDER')].sort_values(by='COST IN(CR.)',ascending = False).head(5)


# In[90]:


ipl=ipl.rename(columns={'2021 Squad':'Prev_team'})


# In[91]:


unsold_players = ipl[(ipl.Prev_team != 'Not Participated')& (ipl.Team == 'Unsold')][['Player','Prev_team']]


# In[92]:


print(unsold_players)


# In[93]:


ipl.head()


# In[94]:


ipl.to_excel(r'F:\Downloads\IPl2022.xlsx', index=None, header=True)


# In[ ]:





# In[ ]:




