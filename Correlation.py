#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np


# In[20]:


data_ads= pd.read_csv("C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/ads/Advertising.csv")


# In[21]:


cols=data_ads.columns.values


# In[22]:


cols


# In[ ]:





# In[4]:


data_ads.head(10)


# In[5]:


len(data_ads)


# In[7]:


data_ads["corrn"]=(data_ads["TV"]-np.mean(data_ads["TV"])) * (data_ads["Sales"]-np.mean(data_ads["Sales"]))


# In[8]:


data_ads.head()


# In[9]:


data_ads["corr1"]=(data_ads["TV"]-np.mean(data_ads["TV"]))**2


# In[10]:


data_ads.head()


# In[11]:


data_ads["corr2"]=(data_ads["Sales"]-np.mean(data_ads["Sales"]))**2


# In[12]:


data_ads.head()


# In[15]:


corr_pearson = sum(data_ads["corrn"])/np.sqrt(sum(data_ads["corr1"])*sum(data_ads["corr2"]))


# In[ ]:





# In[17]:


corr_pearson  #Si es positiva quiere decir que entre más se gasta en publicidad en TV mayores son las ventas 


# In[18]:


def corr_coef(df, v1, v2):
    df["corrn"]=(df[v1]-np.mean(df[v1])) * (df[v2]-np.mean(df[v2]))
    df["corr1"]=(df[v1]-np.mean(df[v1]))**2
    df["corr2"]=(df[v2]-np.mean(df[v2]))**2
    corr_pearson = sum(df["corrn"])/np.sqrt(sum(df["corr1"])*sum(df["corr2"]))
    return corr_pearson


# In[19]:


corr_coef(data_ads, "TV", "Sales")


# In[32]:


for i in cols:
    for j in cols:
        print(i + ", "+ j + ": " + str(corr_coef(data_ads, i, j)))
        


# In[34]:


import matplotlib.pyplot as plt


# In[41]:


plt.plot(data_ads["TV"], data_ads["Sales"], "ro")
plt.title("Gasto en TV y ventas obtenidas")
plt.xlabel("Gasto en TV")
plt.ylabel("ventas")


# In[44]:


plt.plot(data_ads["Newspaper"], data_ads["Sales"], "gx")
plt.title("Gasto en Periódico y ventas obtenidas")
plt.xlabel("Gasto en Periódico")
plt.ylabel("ventas")


# In[ ]:





# In[49]:


plt.plot(data_ads["Radio"], data_ads["Sales"], "bo")
plt.title("Gasto en Radio y ventas obtenidas")
plt.xlabel("Gasto en Radio")
plt.ylabel("ventas")


# In[50]:


### Correlación incluida en pandas


# In[51]:


data_ads= pd.read_csv("C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/ads/Advertising.csv")
data_ads.corr()


# In[52]:


plt.matshow(data_ads.corr())


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




