#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv(r"C:\Users\Keertu\Downloads\tourism_dataset_5000.csv")
print(df.isnull())


# In[2]:


print(df.isnull().sum())


# In[3]:


print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df)


# In[5]:


Q1 = df['Tourist Rating'].quantile(0.25)
Q3 = df['Tourist Rating'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Tourist Rating'] < lower) |
              (df['Tourist Rating'] > upper)]

print(outliers)


# In[6]:


print(df.columns)


# In[7]:


Q1 = df['Tourist Rating'].quantile(0.25)
Q3 = df['Tourist Rating'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower)
print("Upper Bound:", upper)


# In[8]:


from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

categorical_columns = ['Interests', 'Accessibility', 'Site Name', 'Route ID']

for col in categorical_columns:
    df[col] = encoder.fit_transform(df[col])

print(df)


# In[9]:


import pandas as pd

df = pd.get_dummies(df, columns=['Interests', 'Accessibility', 'Site Name', 'Route ID'])

print(df)


# In[ ]:




