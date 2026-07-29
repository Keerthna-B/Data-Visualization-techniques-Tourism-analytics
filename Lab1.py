#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to Data Analytics Lab")


# In[2]:


a = 20
b = 10

print("Addition =",a+b) 
print("Subtraction =",a-b) 
print("Multiplication =",a*b) 
print("Division =",a/b)


# In[8]:


name = "Keerthna" 
dept = "CSBS" 
cgpa = 8.9

print("Name:",name) 
print("Department:",dept) 
print("CGPA:",cgpa)



# In[4]:


# Data Analytics Lab
## Experiment 1

### Jupyter Notebook


# In[5]:


import numpy as np
a = np.array([10,20,30,40,50])
print(a)
print("Mean =",np.mean(a))
print("Sum =",np.sum(a))


# In[9]:


import pandas as pd
data = {
'Name':['Keerthna','Sheeba','Deepa'], 
'Marks':[85,90,95]
}

df = pd.DataFrame(data) 
print(df)


# In[7]:


import matplotlib.pyplot as plt 
x=[1,2,3,4,5]
y=[10,20,15,25,30]

plt.plot(x,y)
plt.title("Sample Line Graph") 
plt.xlabel("X Axis") 
plt.ylabel("Y Axis") 
plt.show()



# In[ ]:




