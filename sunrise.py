import pandas as pd
import requests

url = 'https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873'

results = requests.get(url=url)

# print(results.text)
# print(results.json)
# print(results.json())

sunrise = results.json()

# print(sunrise) 
# print(type(sunrise)) 
# print(sunrise['results'])

sunrise_data = sunrise['results'] 
sunrise_data['id']= 'test_123'

print(sunrise_data)

sunrise_data_list = []
sunrise_data_list.append(sunrise_data)

print(type(sunrise_data_list))
print(sunrise_data_list)

df = pd.DataFrame.from_records(sunrise_data_list)

print(df.head())

