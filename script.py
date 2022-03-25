#!/usr/bin/env python
# coding: utf-8

# In[93]:


import requests
import json


# In[94]:


def get_response():
    city = input("Enter the city you want to check")
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid=eb40cd8fe7b3bb3460776fbee82754b2".format(city))
    return response


# In[96]:


response = get_response()


# In[97]:


text = json.dumps(response.json(),sort_keys=True, indent=4)
# print(text)


# In[98]:


def convert_k_to_c(kelvin):
    return kelvin - 273.15


# In[99]:


def convert_c_to_f(celcius):
    return (celcius * 1.8) + 32


# In[100]:


def convert_k_to_f(kelvin):
    celcius = convert_k_to_c(kelvin)
    output = convert_c_to_f(celcius)
    return output


# In[109]:


def print_temps():
    print("Current weather for " + response.json()['name'])
    print("Current temperature: " + str(round(convert_k_to_f(response.json()['main']['temp']),2)) + " F")
    feels_like = round(convert_k_to_f(response.json()['main']['feels_like']),2)
    print("Feels like: " + str(feels_like) + " F")
    humidity = response.json()['main']['humidity']
    print("Humidity: " + str(humidity))
    high_temp = round(convert_k_to_f(response.json()['main']['temp_max']))
    print("High: " + str(round(high_temp,2)) + " F")
    low_temp = round(convert_k_to_f(response.json()['main']['temp_min']))
    print("Low: " + str(round(low_temp,2)) + " F")
print_temps()

