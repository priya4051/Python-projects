#!/usr/bin/env python
# coding: utf-8

# import plotly.express as px: This imports the Plotly Express module and assigns it the alias px. Plotly Express is a high-level interface for creating easy-to-use, interactive visualizations. It simplifies the process of creating complex plots by providing a simple and intuitive syntax.
# 
# import plotly.graph_objects as go: This imports the Graph Objects module from Plotly and assigns it the alias go. Plotly Graph Objects provides a low-level interface for creating highly customizable plots and charts. While it offers more control over the appearance and behavior of the plots, it also requires more code compared to Plotly Express.

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
data= pd.read_csv(r"C:\Users\priya\Downloads\Screentime-App-Details.csv")
print(data.head())


# In[2]:


data.info()


# In[4]:


data.isnull().sum()


# In[5]:


print(data.describe())


# In[7]:


figure=px.bar(data_frame=data,
             x="Date",
             y="Usage",
             color="App",
             title="Usage")

figure.show()


# In[10]:


figure= px.bar(data_frame=data,
              x="Date",
              y="Notifications",
               color="App",
              title="Notifications")
figure.show()


# In[11]:


figure=px.bar(data_frame=data,
             x="Date",
             y="Times opened",
             color="App",
             title="Times opened")
figure.show()


# In[12]:


figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()


# #There’s a linear relationship between the number of notifications and the amount of usage. It means that more notifications result in more use of smartphones
# 
# So this is how we can analyze the screen time of a user using the Python programming language. Screen Time Analysis is the task of analyzing and creating a report on which applications and websites are used by the user for how much time. 
