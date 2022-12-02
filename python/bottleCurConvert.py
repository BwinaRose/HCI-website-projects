from bottle import route, run, view, static_file
import APIkey as api
import requests


@route('/')
@view("pages/currencyConvert")
def main():
    baseUrl = f"https://v6.exchangerate-api.com/v6/{api.CurrencyAPI}/pair/"
    currencyFrom = 'USD'
    currencyTo = 'JPY'
    currencyTo2 = 'HKD'
    url = f'{baseUrl}/{currencyFrom}/{currencyTo}'
    url2 = f'{baseUrl}/{currencyFrom}/{currencyTo2}'
    json = requests.get(url).json()
    json2 = requests.get(url2).json()
    # print(json) # <----- for debugging
    rate = json['conversion_rate']
    rate2 = json2['conversion_rate']

    return dict(currencyFrom=currencyFrom,
                currencyTo=currencyTo,
                currencyTo2=currencyTo2,
                rate=rate,
                rate2=rate2)


@route('/static/css/style.css')
def send_css():
    return static_file("style.css", "static/css")


run(host='localhost', port=8085, debug=True, reloader=True)