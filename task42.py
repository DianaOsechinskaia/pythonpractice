import requests


def currency_rates(ex):
    URL = 'https://www.cbr-xml-daily.ru/daily_json.js'
    list = {}
    try:
      response = requests.get(url=URL)
      data = response.json()['Valute'][ex]
      list = data
      print('Курс', ex, 'на сегодняшний день в RUB:')
      print(list['Value'])
      print(type(list['Value']))
    except:
     print('NONE')





currency_rates('GBP')