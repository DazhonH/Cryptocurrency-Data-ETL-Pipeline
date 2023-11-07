#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7cc2c3d0-1d08-4ad3-91fe-289bbb58631e',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[5]:


import pandas as pd 

pd.set_option('display.max_columns', None)
crypto = pd.json_normalize(data['data'])

crypto.head(5)


# In[6]:


crypto.info()


# In[7]:


#Converting date colimns to date time

crypto['date_added'] = pd.to_datetime(crypto['date_added'])
crypto['last_updated'] = pd.to_datetime(crypto['last_updated'])
crypto['quote.USD.last_updated'] = pd.to_datetime(crypto['quote.USD.last_updated'])

crypto.info()


# In[8]:


# Adding Columns Weekday, Day, Month, Month Names, and Year

crypto["weekday"] = crypto["quote.USD.last_updated"].dt.day_name()
crypto["day"] = crypto["quote.USD.last_updated"].dt.day
crypto["month"] = crypto["quote.USD.last_updated"].dt.month
crypto["month_name"] = crypto["quote.USD.last_updated"].dt.month_name()
crypto["year"] = crypto["quote.USD.last_updated"].dt.year

crypto.head(5)


# In[ ]:


#Dropping unnecessary columns 

crypto.drop(['platform','self_reported_circulating_supply',
             'self_reported_market_cap','tvl_ratio',
            'platform.id','platform.name','platform.symbol',
            'platform.slug','platform.token_address'],axis=1)


# In[24]:


crypto.info()


# In[27]:


print("Shape of dataset  ",crypto.shape)
print("# of rows in dataset  ",crypto.shape[0])
print("# of columns in dataset  ",crypto.shape[1])


# In[32]:


# Push to CSV

crypto.to_csv('Crypto_API_Data.csv')


# In[ ]:


#Import gbq
from pandas.io import gbq


# In[60]:


# Import CSV Data
cmc = pd.read_csv('/Users/dazhonhunt/Crypto_API_Data.csv')

cmc.head(5)


# In[61]:


# Connect to Google CLoud API to Upload Crypto Dataframe
cmc.to_gbq(destination_table='cmc_API_11623.cmc_data',
           project_id='crypto-df-load',
          if_exists='fail')


# In[ ]:




