#!/usr/bin/env python
# coding: utf-8

# In[56]:


import requests
import json


# In[57]:


def get_response():
    city = input("Enter the city you want to check")
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=eb40cd8fe7b3bb3460776fbee82754b2".format(city))
    return response


# In[58]:


# response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=dallas&appid=eb40cd8fe7b3bb3460776fbee82754b2")


# In[59]:


response = get_response()


# In[60]:


text = json.dumps(response.json(),sort_keys=True, indent=4)
print(text)


# In[61]:


test = response.json()['main']['temp']
print(test)


# In[62]:


def convert_k_to_c(kelvin):
    return kelvin - 273.15


# In[63]:


def convert_c_to_f(celcius):
    return (celcius * 1.8) + 32


# In[64]:


def convert_k_to_f(kelvin):
    celcius = convert_k_to_c(kelvin)
    output = convert_c_to_f(celcius)
    return output


# In[65]:


print(convert_k_to_f(response.json()['main']['temp']))

