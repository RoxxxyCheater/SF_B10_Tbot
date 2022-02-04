import requests
import json
from support import keys
from decimal import Decimal
import time

errors_log = []

class ConvExeption(Exception):
    print(Exception)


class WrongTransaction(Exception):
    @staticmethod
    def control(curr_from: str, curr_to: str, amount: any((str,float)), name):
        time_string = time.strftime("%H:%M:%S", time.localtime())
        if curr_to == curr_from:
            errors_log.append(f'[{name}, {time_string}, {curr_from}, {curr_to}, {amount}, the same curr]')
            raise WrongTransaction('You can`t convert the same currents: Нельзя выбрать одну и ту же валюту.')
        try:
            in_tiker = keys[curr_from]
        except KeyError as e:
            errors_log.append(f'[{name}, {time_string}, {curr_from}, {e}]')
            raise ConvExeption(f'Ошибка при индефикации 1 валюты "{curr_from}"')
        try:
            out_tiker = keys[curr_to]
        except KeyError as e:
            errors_log.append(f'[{name}, {time_string}, {curr_to}, {e}]')
            raise ConvExeption(f'Ошибка при индефикации 2 валюты "{curr_to}"')
        try:
            amount = float(amount)
        except KeyError as e:
            errors_log.append(f'[{name}, {time_string}, {amount}, {e}]')
            raise ConvExeption(f'Ошибка при индефикации колл-ва указанных едениц{amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={curr_from}&tsyms={curr_to}')
        res = Decimal(json.loads(r.content)[curr_to])
        return res


#r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=9d75eb30bcbea514fcbbfb2343c49af8')