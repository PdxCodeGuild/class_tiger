
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
from copy import copy
import datetime
import numpy as np
import seaborn as sns
from scipy.stats import mode

def load_data():
    '''Loads data and removes unwanted first lines'''
    with open('maplewood.txt', 'r') as f: #note a csv is a text becuz ,seperated
        raw = f.read().split('\n')
        '''remove empty lines give back lines that don't start and end with space'''
        remove_empty_lines = [line for line in raw if line.strip() != '']
        '''remove unwanted first 7 lines'''
        semi = remove_empty_lines[7:len(remove_empty_lines)]
        '''get header & remove duplicated empty spaces'''
        header = semi.pop(0).strip().split()
        '''only two columns needed'''
        header = header[0:2]
        '''get data  part'''
        semi = semi[1:len(semi)]
        data = [] #create a list
        dates =[]
        values =[]
        for i in range(len(semi)):
            comma_sep_v_list = semi[i].lower().strip().split()
            data.append(comma_sep_v_list[0:2])
        return data, header

data,header = load_data()
'''turns into pandas dataframe'''
df = pd.DataFrame(data)


# In[47]:


df.head()


# In[48]:


df.info()


# In[49]:


# Drop rows with missing values and drop duplicate
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)


# In[50]:


df.describe()


# In[51]:


'''convert 1st column from string to dates'''
df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
'''convert second column to int non digit will become Nan'''
#df.iloc[:,1] = pd.to_numeric(df.iloc[:,1], errors='coerce')
df.iloc[:,1] = pd.to_numeric(df.iloc[:,1], errors='coerce').fillna(0).astype(np.int64)
'''drop NA'''
df.dropna(how='all')
'''Add a year, month column'''
df['year']= df.iloc[:,0].dt.year
df['month']= df.iloc[:,0].dt.month
df['day']= df.iloc[:,0].dt.day;


# In[52]:


df.head()


# In[53]:


'''renaming columns for ease'''
df.rename(columns={0:'dates',
                          1:'rain',
                          'year':'year',
                          'month': 'month',
                          'day': 'day'
                          },
                 inplace=True)


# In[54]:


df_by_year = df.groupby('year')


# In[55]:


type(df_by_year)


# In[56]:


df_by_year.describe().head()


# In[57]:


df_mean_by_year = df_by_year.mean()


# In[58]:


df_mean_by_year


# In[60]:


'''To plot index the column in df with mean from grouping'''
df_rain_by_year = df_mean_by_year['rain']
plt.bar(df_rain_by_year.index, df_rain_by_year)
plt.xlabel('year')
plt.ylabel('average rain');


# In[61]:


df_by_month = df.groupby('month')
df_mean_by_month = df_by_month.mean()


# In[62]:


df_rain_by_month = df_mean_by_month['rain']
plt.bar(df_rain_by_month.index, df_rain_by_month)
plt.xlabel('month')
plt.ylabel('average rain');


# In[63]:


df_total_by_year = df_by_year.sum()


# In[64]:


'''To plot index the column in df with mean from grouping'''
df_rain_by_year = df_total_by_year['rain']
plt.bar(df_rain_by_year.index, df_rain_by_year)
plt.xlabel('year')
plt.ylabel('total rain');

