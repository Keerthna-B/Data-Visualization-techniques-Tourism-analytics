#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
df=pd.read_csv(r"C:\Users\Keertu\Downloads\tourism_dataset_5000.csv")
print(df)



# In[2]:


print(df.head())


# In[3]:


print(df.info())


# In[4]:


print(df.describe())


# In[ ]:





# In[11]:


import sqlite3
conn=sqlite3.connect("student.db")
cursor=conn.cursor()
cursor.execute("""
create table if not exists students(
id integer primary key,
name text,
age integer,
department text
)
""")
cursor.execute("insert into students(name,age,department) values('keertu',19,'CSBS')")
cursor.execute("insert into students(name,age,department) values('shabu',28,'Architecture')")
conn.commit()
conn.close()
print("database created sucessfully")


# In[15]:


import sqlite3
import pandas as pd
conn=sqlite3.connect("student.db")
query="select *from students"
df=pd.read_sql(query,conn)
print(df)


# In[18]:


data={
    "Name":["keerthu","shabu","dabu"],
    "Age":[19,28,30],
    "department":["CSBS","Architecture","Engineer"],
    "Id":[1,2,3]
}
df=pd.DataFrame(data)
df.to_excel("output.xlsx",index=False)
print("Excel File Exported")


# In[21]:


df.to_json("output.json",orient="records",indent=4)
print("JSON file exported")


# In[22]:


df.to_sql("students",conn,if_exists="replace",index=False)
print("sql exported")


# In[ ]:




