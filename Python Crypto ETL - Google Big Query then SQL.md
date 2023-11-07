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


```python
import pandas as pd 

pd.set_option('display.max_columns', None)
crypto = pd.json_normalize(data['data'])

crypto.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>symbol</th>
      <th>slug</th>
      <th>num_market_pairs</th>
      <th>date_added</th>
      <th>tags</th>
      <th>max_supply</th>
      <th>circulating_supply</th>
      <th>total_supply</th>
      <th>infinite_supply</th>
      <th>platform</th>
      <th>cmc_rank</th>
      <th>self_reported_circulating_supply</th>
      <th>self_reported_market_cap</th>
      <th>tvl_ratio</th>
      <th>last_updated</th>
      <th>quote.USD.price</th>
      <th>quote.USD.volume_24h</th>
      <th>quote.USD.volume_change_24h</th>
      <th>quote.USD.percent_change_1h</th>
      <th>quote.USD.percent_change_24h</th>
      <th>quote.USD.percent_change_7d</th>
      <th>quote.USD.percent_change_30d</th>
      <th>quote.USD.percent_change_60d</th>
      <th>quote.USD.percent_change_90d</th>
      <th>quote.USD.market_cap</th>
      <th>quote.USD.market_cap_dominance</th>
      <th>quote.USD.fully_diluted_market_cap</th>
      <th>quote.USD.tvl</th>
      <th>quote.USD.last_updated</th>
      <th>platform.id</th>
      <th>platform.name</th>
      <th>platform.symbol</th>
      <th>platform.slug</th>
      <th>platform.token_address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>10520</td>
      <td>2010-07-13T00:00:00.000Z</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>2.100000e+07</td>
      <td>1.953429e+07</td>
      <td>19534287</td>
      <td>False</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05T20:53:00.000Z</td>
      <td>35044.358127</td>
      <td>1.172220e+10</td>
      <td>31.6648</td>
      <td>0.014302</td>
      <td>0.762015</td>
      <td>1.235549</td>
      <td>25.202601</td>
      <td>36.457470</td>
      <td>20.245804</td>
      <td>6.845665e+11</td>
      <td>51.8954</td>
      <td>7.359315e+11</td>
      <td>NaN</td>
      <td>2023-11-05T20:53:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>7706</td>
      <td>2015-08-07T00:00:00.000Z</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>1.202689e+08</td>
      <td>120268913.449319</td>
      <td>True</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05T20:53:00.000Z</td>
      <td>1888.030966</td>
      <td>8.261641e+09</td>
      <td>76.8321</td>
      <td>-0.232300</td>
      <td>2.602390</td>
      <td>5.027772</td>
      <td>14.586662</td>
      <td>15.925903</td>
      <td>3.482617</td>
      <td>2.270714e+11</td>
      <td>17.2130</td>
      <td>2.270714e+11</td>
      <td>NaN</td>
      <td>2023-11-05T20:53:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether USDt</td>
      <td>USDT</td>
      <td>tether</td>
      <td>65115</td>
      <td>2015-02-25T00:00:00.000Z</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>8.536776e+10</td>
      <td>88623656723.666138</td>
      <td>True</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05T20:52:00.000Z</td>
      <td>1.000806</td>
      <td>2.637396e+10</td>
      <td>35.1081</td>
      <td>0.004969</td>
      <td>0.009829</td>
      <td>0.040495</td>
      <td>0.033400</td>
      <td>0.144410</td>
      <td>0.203207</td>
      <td>8.543658e+10</td>
      <td>6.4765</td>
      <td>8.869511e+10</td>
      <td>NaN</td>
      <td>2023-11-05T20:52:00.000Z</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1740</td>
      <td>2017-07-25T00:00:00.000Z</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>NaN</td>
      <td>1.517029e+08</td>
      <td>151702859.540038</td>
      <td>False</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05T20:52:00.000Z</td>
      <td>244.077994</td>
      <td>3.999517e+08</td>
      <td>53.2776</td>
      <td>0.138847</td>
      <td>3.284135</td>
      <td>7.464930</td>
      <td>14.272960</td>
      <td>13.688345</td>
      <td>1.045233</td>
      <td>3.702733e+10</td>
      <td>2.8070</td>
      <td>3.702733e+10</td>
      <td>NaN</td>
      <td>2023-11-05T20:52:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>1132</td>
      <td>2013-08-04T00:00:00.000Z</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>1.000000e+11</td>
      <td>5.361584e+10</td>
      <td>99988316618</td>
      <td>False</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05T20:53:00.000Z</td>
      <td>0.652994</td>
      <td>1.808787e+09</td>
      <td>117.8713</td>
      <td>-0.686438</td>
      <td>6.455816</td>
      <td>16.662828</td>
      <td>23.930635</td>
      <td>30.301753</td>
      <td>5.979459</td>
      <td>3.501082e+10</td>
      <td>2.6540</td>
      <td>6.529940e+10</td>
      <td>NaN</td>
      <td>2023-11-05T20:53:00.000Z</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
crypto.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5000 entries, 0 to 4999
    Data columns (total 36 columns):
     #   Column                              Non-Null Count  Dtype  
    ---  ------                              --------------  -----  
     0   id                                  5000 non-null   int64  
     1   name                                5000 non-null   object 
     2   symbol                              5000 non-null   object 
     3   slug                                5000 non-null   object 
     4   num_market_pairs                    5000 non-null   int64  
     5   date_added                          5000 non-null   object 
     6   tags                                5000 non-null   object 
     7   max_supply                          3773 non-null   float64
     8   circulating_supply                  5000 non-null   float64
     9   total_supply                        5000 non-null   object 
     10  infinite_supply                     5000 non-null   bool   
     11  platform                            0 non-null      float64
     12  cmc_rank                            5000 non-null   int64  
     13  self_reported_circulating_supply    2733 non-null   float64
     14  self_reported_market_cap            2733 non-null   float64
     15  tvl_ratio                           83 non-null     float64
     16  last_updated                        5000 non-null   object 
     17  quote.USD.price                     5000 non-null   float64
     18  quote.USD.volume_24h                5000 non-null   float64
     19  quote.USD.volume_change_24h         5000 non-null   float64
     20  quote.USD.percent_change_1h         5000 non-null   float64
     21  quote.USD.percent_change_24h        5000 non-null   float64
     22  quote.USD.percent_change_7d         5000 non-null   float64
     23  quote.USD.percent_change_30d        5000 non-null   float64
     24  quote.USD.percent_change_60d        5000 non-null   float64
     25  quote.USD.percent_change_90d        5000 non-null   float64
     26  quote.USD.market_cap                5000 non-null   float64
     27  quote.USD.market_cap_dominance      5000 non-null   float64
     28  quote.USD.fully_diluted_market_cap  5000 non-null   float64
     29  quote.USD.tvl                       89 non-null     float64
     30  quote.USD.last_updated              5000 non-null   object 
     31  platform.id                         4254 non-null   float64
     32  platform.name                       4254 non-null   object 
     33  platform.symbol                     4254 non-null   object 
     34  platform.slug                       4254 non-null   object 
     35  platform.token_address              4254 non-null   object 
    dtypes: bool(1), float64(20), int64(3), object(12)
    memory usage: 1.3+ MB



```python
#Converting date colimns to date time

crypto['date_added'] = pd.to_datetime(crypto['date_added'])
crypto['last_updated'] = pd.to_datetime(crypto['last_updated'])
crypto['quote.USD.last_updated'] = pd.to_datetime(crypto['quote.USD.last_updated'])

crypto.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5000 entries, 0 to 4999
    Data columns (total 36 columns):
     #   Column                              Non-Null Count  Dtype              
    ---  ------                              --------------  -----              
     0   id                                  5000 non-null   int64              
     1   name                                5000 non-null   object             
     2   symbol                              5000 non-null   object             
     3   slug                                5000 non-null   object             
     4   num_market_pairs                    5000 non-null   int64              
     5   date_added                          5000 non-null   datetime64[ns, UTC]
     6   tags                                5000 non-null   object             
     7   max_supply                          3773 non-null   float64            
     8   circulating_supply                  5000 non-null   float64            
     9   total_supply                        5000 non-null   object             
     10  infinite_supply                     5000 non-null   bool               
     11  platform                            0 non-null      float64            
     12  cmc_rank                            5000 non-null   int64              
     13  self_reported_circulating_supply    2733 non-null   float64            
     14  self_reported_market_cap            2733 non-null   float64            
     15  tvl_ratio                           83 non-null     float64            
     16  last_updated                        5000 non-null   datetime64[ns, UTC]
     17  quote.USD.price                     5000 non-null   float64            
     18  quote.USD.volume_24h                5000 non-null   float64            
     19  quote.USD.volume_change_24h         5000 non-null   float64            
     20  quote.USD.percent_change_1h         5000 non-null   float64            
     21  quote.USD.percent_change_24h        5000 non-null   float64            
     22  quote.USD.percent_change_7d         5000 non-null   float64            
     23  quote.USD.percent_change_30d        5000 non-null   float64            
     24  quote.USD.percent_change_60d        5000 non-null   float64            
     25  quote.USD.percent_change_90d        5000 non-null   float64            
     26  quote.USD.market_cap                5000 non-null   float64            
     27  quote.USD.market_cap_dominance      5000 non-null   float64            
     28  quote.USD.fully_diluted_market_cap  5000 non-null   float64            
     29  quote.USD.tvl                       89 non-null     float64            
     30  quote.USD.last_updated              5000 non-null   datetime64[ns, UTC]
     31  platform.id                         4254 non-null   float64            
     32  platform.name                       4254 non-null   object             
     33  platform.symbol                     4254 non-null   object             
     34  platform.slug                       4254 non-null   object             
     35  platform.token_address              4254 non-null   object             
    dtypes: bool(1), datetime64[ns, UTC](3), float64(20), int64(3), object(9)
    memory usage: 1.3+ MB



```python
# Adding Columns Weekday, Day, Month, Month Names, and Year

crypto["weekday"] = crypto["quote.USD.last_updated"].dt.day_name()
crypto["day"] = crypto["quote.USD.last_updated"].dt.day
crypto["month"] = crypto["quote.USD.last_updated"].dt.month
crypto["month_name"] = crypto["quote.USD.last_updated"].dt.month_name()
crypto["year"] = crypto["quote.USD.last_updated"].dt.year

crypto.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>symbol</th>
      <th>slug</th>
      <th>num_market_pairs</th>
      <th>date_added</th>
      <th>tags</th>
      <th>max_supply</th>
      <th>circulating_supply</th>
      <th>total_supply</th>
      <th>infinite_supply</th>
      <th>platform</th>
      <th>cmc_rank</th>
      <th>self_reported_circulating_supply</th>
      <th>self_reported_market_cap</th>
      <th>tvl_ratio</th>
      <th>last_updated</th>
      <th>quote.USD.price</th>
      <th>quote.USD.volume_24h</th>
      <th>quote.USD.volume_change_24h</th>
      <th>quote.USD.percent_change_1h</th>
      <th>quote.USD.percent_change_24h</th>
      <th>quote.USD.percent_change_7d</th>
      <th>quote.USD.percent_change_30d</th>
      <th>quote.USD.percent_change_60d</th>
      <th>quote.USD.percent_change_90d</th>
      <th>quote.USD.market_cap</th>
      <th>quote.USD.market_cap_dominance</th>
      <th>quote.USD.fully_diluted_market_cap</th>
      <th>quote.USD.tvl</th>
      <th>quote.USD.last_updated</th>
      <th>platform.id</th>
      <th>platform.name</th>
      <th>platform.symbol</th>
      <th>platform.slug</th>
      <th>platform.token_address</th>
      <th>weekday</th>
      <th>day</th>
      <th>month</th>
      <th>month_name</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>10520</td>
      <td>2010-07-13 00:00:00+00:00</td>
      <td>[mineable, pow, sha-256, store-of-value, state...</td>
      <td>2.100000e+07</td>
      <td>1.953429e+07</td>
      <td>19534287</td>
      <td>False</td>
      <td>NaN</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>35044.358127</td>
      <td>1.172220e+10</td>
      <td>31.6648</td>
      <td>0.014302</td>
      <td>0.762015</td>
      <td>1.235549</td>
      <td>25.202601</td>
      <td>36.457470</td>
      <td>20.245804</td>
      <td>6.845665e+11</td>
      <td>51.8954</td>
      <td>7.359315e+11</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>7706</td>
      <td>2015-08-07 00:00:00+00:00</td>
      <td>[pos, smart-contracts, ethereum-ecosystem, coi...</td>
      <td>NaN</td>
      <td>1.202689e+08</td>
      <td>120268913.449319</td>
      <td>True</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>1888.030966</td>
      <td>8.261641e+09</td>
      <td>76.8321</td>
      <td>-0.232300</td>
      <td>2.602390</td>
      <td>5.027772</td>
      <td>14.586662</td>
      <td>15.925903</td>
      <td>3.482617</td>
      <td>2.270714e+11</td>
      <td>17.2130</td>
      <td>2.270714e+11</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether USDt</td>
      <td>USDT</td>
      <td>tether</td>
      <td>65115</td>
      <td>2015-02-25 00:00:00+00:00</td>
      <td>[payments, stablecoin, asset-backed-stablecoin...</td>
      <td>NaN</td>
      <td>8.536776e+10</td>
      <td>88623656723.666138</td>
      <td>True</td>
      <td>NaN</td>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>1.000806</td>
      <td>2.637396e+10</td>
      <td>35.1081</td>
      <td>0.004969</td>
      <td>0.009829</td>
      <td>0.040495</td>
      <td>0.033400</td>
      <td>0.144410</td>
      <td>0.203207</td>
      <td>8.543658e+10</td>
      <td>6.4765</td>
      <td>8.869511e+10</td>
      <td>NaN</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>1027.0</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>0xdac17f958d2ee523a2206206994597c13d831ec7</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1740</td>
      <td>2017-07-25 00:00:00+00:00</td>
      <td>[marketplace, centralized-exchange, payments, ...</td>
      <td>NaN</td>
      <td>1.517029e+08</td>
      <td>151702859.540038</td>
      <td>False</td>
      <td>NaN</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>244.077994</td>
      <td>3.999517e+08</td>
      <td>53.2776</td>
      <td>0.138847</td>
      <td>3.284135</td>
      <td>7.464930</td>
      <td>14.272960</td>
      <td>13.688345</td>
      <td>1.045233</td>
      <td>3.702733e+10</td>
      <td>2.8070</td>
      <td>3.702733e+10</td>
      <td>NaN</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>1132</td>
      <td>2013-08-04 00:00:00+00:00</td>
      <td>[medium-of-exchange, enterprise-solutions, arr...</td>
      <td>1.000000e+11</td>
      <td>5.361584e+10</td>
      <td>99988316618</td>
      <td>False</td>
      <td>NaN</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>0.652994</td>
      <td>1.808787e+09</td>
      <td>117.8713</td>
      <td>-0.686438</td>
      <td>6.455816</td>
      <td>16.662828</td>
      <td>23.930635</td>
      <td>30.301753</td>
      <td>5.979459</td>
      <td>3.501082e+10</td>
      <td>2.6540</td>
      <td>6.529940e+10</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Dropping unnecessary columns 

crypto.drop(['platform','self_reported_circulating_supply',
             'self_reported_market_cap','tvl_ratio',
            'platform.id','platform.name','platform.symbol',
            'platform.slug','platform.token_address'],axis=1)

```


```python
crypto.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 5000 entries, 0 to 4999
    Data columns (total 32 columns):
     #   Column                              Non-Null Count  Dtype              
    ---  ------                              --------------  -----              
     0   id                                  5000 non-null   int64              
     1   name                                5000 non-null   object             
     2   symbol                              5000 non-null   object             
     3   slug                                5000 non-null   object             
     4   num_market_pairs                    5000 non-null   int64              
     5   date_added                          5000 non-null   datetime64[ns, UTC]
     6   tags                                5000 non-null   object             
     7   max_supply                          3773 non-null   float64            
     8   circulating_supply                  5000 non-null   float64            
     9   total_supply                        5000 non-null   object             
     10  infinite_supply                     5000 non-null   bool               
     11  cmc_rank                            5000 non-null   int64              
     12  last_updated                        5000 non-null   datetime64[ns, UTC]
     13  quote.USD.price                     5000 non-null   float64            
     14  quote.USD.volume_24h                5000 non-null   float64            
     15  quote.USD.volume_change_24h         5000 non-null   float64            
     16  quote.USD.percent_change_1h         5000 non-null   float64            
     17  quote.USD.percent_change_24h        5000 non-null   float64            
     18  quote.USD.percent_change_7d         5000 non-null   float64            
     19  quote.USD.percent_change_30d        5000 non-null   float64            
     20  quote.USD.percent_change_60d        5000 non-null   float64            
     21  quote.USD.percent_change_90d        5000 non-null   float64            
     22  quote.USD.market_cap                5000 non-null   float64            
     23  quote.USD.market_cap_dominance      5000 non-null   float64            
     24  quote.USD.fully_diluted_market_cap  5000 non-null   float64            
     25  quote.USD.tvl                       89 non-null     float64            
     26  quote.USD.last_updated              5000 non-null   datetime64[ns, UTC]
     27  weekday                             5000 non-null   object             
     28  day                                 5000 non-null   int64              
     29  month                               5000 non-null   int64              
     30  month_name                          5000 non-null   object             
     31  year                                5000 non-null   int64              
    dtypes: bool(1), datetime64[ns, UTC](3), float64(15), int64(6), object(7)
    memory usage: 1.2+ MB



```python
print("Shape of dataset  ",crypto.shape)
print("# of rows in dataset  ",crypto.shape[0])
print("# of columns in dataset  ",crypto.shape[1])
```

    Shape of dataset   (5000, 32)
    # of rows in dataset   5000
    # of columns in dataset   32



```python
# Push to CSV

crypto.to_csv('Crypto_API_Data.csv')
```


```python
#Import gbq
from pandas.io import gbq

```


```python
# Import CSV Data
cmc = pd.read_csv('/Users/dazhonhunt/Crypto_API_Data.csv')

cmc.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>name</th>
      <th>symbol</th>
      <th>slug</th>
      <th>num_market_pairs</th>
      <th>date_added</th>
      <th>tags</th>
      <th>max_supply</th>
      <th>circulating_supply</th>
      <th>total_supply</th>
      <th>infinite_supply</th>
      <th>cmc_rank</th>
      <th>last_updated</th>
      <th>quote_USD_price</th>
      <th>quote_USD_volume_24h</th>
      <th>quote_USD_volume_change_24h</th>
      <th>quote_USD_percent_change_1h</th>
      <th>quote_USD_percent_change_24h</th>
      <th>quote_USD_percent_change_7d</th>
      <th>quote_USD_percent_change_30d</th>
      <th>quote_USD_percent_change_60d</th>
      <th>quote_USD_percent_change_90d</th>
      <th>quote_USD_market_cap</th>
      <th>quote_USD_market_cap_dominance</th>
      <th>quote_USD_fully_diluted_market_cap</th>
      <th>quote_USD_tvl</th>
      <th>quote_USD_last_updated</th>
      <th>weekday</th>
      <th>day</th>
      <th>month</th>
      <th>month_name</th>
      <th>year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Bitcoin</td>
      <td>BTC</td>
      <td>bitcoin</td>
      <td>10520</td>
      <td>2010-07-13 00:00:00+00:00</td>
      <td>['mineable', 'pow', 'sha-256', 'store-of-value...</td>
      <td>2.100000e+07</td>
      <td>1.953429e+07</td>
      <td>1.953429e+07</td>
      <td>False</td>
      <td>1</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>35044.358130</td>
      <td>1.172220e+10</td>
      <td>31.6648</td>
      <td>0.014302</td>
      <td>0.762015</td>
      <td>1.235549</td>
      <td>25.202601</td>
      <td>36.457470</td>
      <td>20.245804</td>
      <td>6.845670e+11</td>
      <td>51.8954</td>
      <td>7.359320e+11</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1027</td>
      <td>Ethereum</td>
      <td>ETH</td>
      <td>ethereum</td>
      <td>7706</td>
      <td>2015-08-07 00:00:00+00:00</td>
      <td>['pos', 'smart-contracts', 'ethereum-ecosystem...</td>
      <td>NaN</td>
      <td>1.202689e+08</td>
      <td>1.202689e+08</td>
      <td>True</td>
      <td>2</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>1888.030966</td>
      <td>8.261641e+09</td>
      <td>76.8321</td>
      <td>-0.232300</td>
      <td>2.602390</td>
      <td>5.027772</td>
      <td>14.586662</td>
      <td>15.925903</td>
      <td>3.482617</td>
      <td>2.270710e+11</td>
      <td>17.2130</td>
      <td>2.270710e+11</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>2</th>
      <td>825</td>
      <td>Tether USDt</td>
      <td>USDT</td>
      <td>tether</td>
      <td>65115</td>
      <td>2015-02-25 00:00:00+00:00</td>
      <td>['payments', 'stablecoin', 'asset-backed-stabl...</td>
      <td>NaN</td>
      <td>8.536776e+10</td>
      <td>8.862366e+10</td>
      <td>True</td>
      <td>3</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>1.000806</td>
      <td>2.637396e+10</td>
      <td>35.1081</td>
      <td>0.004969</td>
      <td>0.009829</td>
      <td>0.040495</td>
      <td>0.033400</td>
      <td>0.144410</td>
      <td>0.203207</td>
      <td>8.543658e+10</td>
      <td>6.4765</td>
      <td>8.869511e+10</td>
      <td>NaN</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1839</td>
      <td>BNB</td>
      <td>BNB</td>
      <td>bnb</td>
      <td>1740</td>
      <td>2017-07-25 00:00:00+00:00</td>
      <td>['marketplace', 'centralized-exchange', 'payme...</td>
      <td>NaN</td>
      <td>1.517029e+08</td>
      <td>1.517029e+08</td>
      <td>False</td>
      <td>4</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>244.077993</td>
      <td>3.999517e+08</td>
      <td>53.2776</td>
      <td>0.138847</td>
      <td>3.284135</td>
      <td>7.464930</td>
      <td>14.272960</td>
      <td>13.688345</td>
      <td>1.045233</td>
      <td>3.702733e+10</td>
      <td>2.8070</td>
      <td>3.702733e+10</td>
      <td>NaN</td>
      <td>2023-11-05 20:52:00+00:00</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
    <tr>
      <th>4</th>
      <td>52</td>
      <td>XRP</td>
      <td>XRP</td>
      <td>xrp</td>
      <td>1132</td>
      <td>2013-08-04 00:00:00+00:00</td>
      <td>['medium-of-exchange', 'enterprise-solutions',...</td>
      <td>1.000000e+11</td>
      <td>5.361584e+10</td>
      <td>9.998832e+10</td>
      <td>False</td>
      <td>5</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>0.652994</td>
      <td>1.808787e+09</td>
      <td>117.8713</td>
      <td>-0.686438</td>
      <td>6.455816</td>
      <td>16.662828</td>
      <td>23.930635</td>
      <td>30.301753</td>
      <td>5.979459</td>
      <td>3.501082e+10</td>
      <td>2.6540</td>
      <td>6.529940e+10</td>
      <td>NaN</td>
      <td>2023-11-05 20:53:00+00:00</td>
      <td>Sunday</td>
      <td>5</td>
      <td>11</td>
      <td>November</td>
      <td>2023</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Connect to Google CLoud API to Upload Crypto Dataframe
cmc.to_gbq(destination_table='cmc_API_11623.cmc_data',
           project_id='crypto-df-load',
          if_exists='fail')
```

    100%|███████████████████████████████████████████| 1/1 [00:00<00:00, 1408.90it/s]



```python

```
