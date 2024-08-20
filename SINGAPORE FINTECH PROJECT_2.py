#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv("../DataSets/Indivisual/individuals-by-tax-group.csv")


# In[3]:


df


# In[4]:


df.dtypes


# In[5]:


df.columns


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[9]:


df.tax_group.value_counts()


# In[10]:


df.nunique()


# In[11]:


sb.pairplot(df)
plt.show()


# In[12]:


df.corr(numeric_only=True)


# # FILTERING AND GROUPING DATA

# In[13]:


S=df.groupby('tax_group')['no_of_indv_assessed'].sum()
S


# In[14]:


R=df.groupby('tax_group')['donations'].sum()
R


# In[15]:


P=df.groupby('tax_group')['assessable_income'].sum()
P


# In[16]:


A=df.groupby('tax_group')['total_income'].sum()
A


# In[18]:


df.nlargest(7,'total_income')


# # DATA VISUALIZATION

# In[20]:


sb.barplot(data=df,x=df.tax_group,y=df.year_of_assessment)
plt.xticks(rotation=90)
plt.xlabel('no of tax group')
plt.ylabel('total no of year assesement')
plt.title('distribution between tax grouop under years')
plt.show()


# In[21]:


s=df.tax_group.value_counts()
s


# In[23]:


plt.pie(s.values,labels=s.index,autopct='%1.1f%%',startangle=90,colors=['red','blue'])
plt.show()


# In[24]:


r=df.corr(numeric_only=True)
r


# In[26]:


sb.heatmap(r.corr(),annot=True,cmap='coolwarm')
plt.xticks(rotation=45)
plt.show()


# In[27]:


plt.figure(figsize=(6,10))
sb.barplot(data=df,x=df.tax_group,y=df.donations)
plt.xlabel('no of tax group')
plt.ylabel('amount of donations')
plt.title('distribution of tax group along with donations')
plt.xticks(rotation=45)
plt.show()


# In[28]:


sb.lineplot(data=df,x=df.year_of_assessment,y=df.total_income)
plt.xlabel('year wise assesement')
plt.ylabel('amount of total income')
plt.title('distribution of year along with amount of total income')
plt.xticks(rotation=45)
plt.show()


# In[29]:


sb.lineplot(data=df,x=df.year_of_assessment,y=df.donations)
plt.xlabel('year wise assesement')
plt.ylabel('amount of total income')
plt.title('distribution of year along with amount of total income')
plt.xticks(rotation=45)
plt.show()


# In[30]:


sb.lineplot(data=df,x=df.year_of_assessment,y=df.assessable_income)
plt.xlabel('year wise assesement')
plt.ylabel('amount of total income')
plt.title('distribution of year along with amount of total income')
plt.xticks(rotation=45)
plt.show()


# In[31]:


plt.figure(figsize=(6,10))
sb.barplot(data=df,x=df.tax_group,y=df.assessable_income)
plt.xlabel('no of tax group')
plt.ylabel('amount of assesemble income')
plt.title('distribution of year along with amount of assesemble income')
plt.xticks(rotation=45)
plt.show()


# # DASHBOARD

# In[32]:


print(df.tax_group.unique())
a=input('enter the  tax group ')
b=df[df.tax_group==a]
b


print(df.year_of_assessment.unique())
c=input('enter the assesement years')
d=df[df.year_of_assessment==c]
d


print(df.donations.unique())
e=input('enter the amount of donations')
f=df[df.donations==e]
f


print(df.assessable_income.unique())
g=input('enter the amount of assessable income')
h=df[df.assessable_income==g]
h


print(df.total_income.unique())
i=input('enter the amount of total income')
j=df[df.total_income==i]
j


# In[33]:


print(df.tax_group.unique())
a=input('enter the  tax group ')
b=df[df.tax_group==a]
plt.figure(figsize=(7,10))
sb.barplot(data=df,x=df.tax_group,y=df.total_income)
plt.xlabel('no.of group type')
plt.ylabel('amount of total income')
plt.title('distribution of tax group along with total income')
plt.xticks(rotation=45)
plt.show()



print(df.year_of_assessment.unique())
c=input('enter the assesement years')
d=df[df.year_of_assessment==c]
plt.figure(figsize=(7,10))
sb.barplot(data=df,x=df.year_of_assessment,y=df.total_income)
plt.xlabel('no.of years')
plt.ylabel('amount of total income')
plt.title('distribution of years  along with total income')
plt.xticks(rotation=45)
plt.show()




print(df.donations.unique())
e=input('enter the amount of donations')
f=df[df.donations==e]
plt.figure(figsize=(7,10))
sb.barplot(data=df,x=df.no_of_indv_assessed,y=df.total_income)
plt.xlabel('no.of assesed individuals')
plt.ylabel('amount of total income')
plt.title('distribution of assesed individuals along with total income')
plt.xticks(rotation=45)
plt.show()




print(df.assessable_income.unique())
g=input('enter the amount of assessable income')
h=df[df.assessable_income==g]
plt.figure(figsize=(7,10))
sb.barplot(data=df,x=df.assessable_income,y=df.total_income)
plt.xlabel('no.of income of assesable')
plt.ylabel('amount of total income')
plt.title('distribution of income of assesable along with total income')
plt.xticks(rotation=45)
plt.show()



print(df.donations.unique())
i=input('enter the amount of donations')
j=df[df.donations==i]
plt.figure(figsize=(7,10))
sb.barplot(data=df,x=df.donations,y=df.total_income)
plt.xlabel('no.of donations')
plt.ylabel('amount of total income')
plt.title('distribution of donations along with total income')
plt.xticks(rotation=45)
plt.show()


# In[ ]:




