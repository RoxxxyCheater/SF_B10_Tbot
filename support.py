import requests
import json


TOKEN = "5176731993:AAGi9FjH0sBd22hvMja625awme-CETeKEBU"

keys = {
    'EUR': 'Euro',
    'USD': 'Dollar',
    'UAH': 'Grivna',
    'RUB': 'Rouble'
}
keys_top = {
    'EUR': 'Euro',
    'USD': 'Dollar',
    'UAH': 'Grivna',
    'RUB': 'Rouble'
}
HELP = f"Что бы начать работу введите комманду боту в формате: \n<Имя валюты> |" \
       f" <в какую валюту хотите перевести> | <Кол-во едениц для конвертации>\n\nПример:" \
       f" BTC USD 20 \n\nУвидеть список TOP100 валют /values"

#добавление всех валют в словарь
r = requests.get(f'https://min-api.cryptocompare.com/data/all/coinlist')
res = json.loads(r.content).get('Data')
for x in res.values():
    keys.update({x['Name']: x['FullName']})

#добавления словаря топ 100
r = requests.get(f'https://min-api.cryptocompare.com/data/top/mktcapfull?limit=100&tsym=USD')
res = json.loads(r.content)
for x in res.get('Data'):
    keys_top.update({x['CoinInfo']['Name']: x['CoinInfo']['FullName']})



