import requests
import APIkey as api

baseUrl = f"https://v6.exchangerate-api.com/v6/{api.CurrencyAPI}/pair/"

currencyFrom = 'USD'
currencyTo = 'JPY'

url = f'{baseUrl}/{currencyFrom}/{currencyTo}'

json = requests.get(url).json()
print(json)  # <----- for debugging

rate = json['conversion_rate']

print(f'Conversion rate from {currencyFrom} to {currencyTo} is {rate}')

#

# html = open("currency.html", "w")
# html.write(f'Conversion rate from {currencyFrom} to {currencyTo} is {rate}')
# html.close()
