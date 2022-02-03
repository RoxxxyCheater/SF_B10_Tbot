import requests
import json
from support import keys, errors_log
from decimal import Decimal
import time


class ConvExeption(Exception):
    print(Exception)
    pass


class WrongTransaction(Exception):
    @staticmethod
    def control(curr_from: str, curr_to: str, amount: any((str,float)), name):
        time_string = time.strftime("%H:%M:%S", time.localtime())
        if curr_to == curr_from:
            raise WrongTransaction('You can`t convert the same currents: Нельзя выбрать одну и ту же валюту.')
        try:
            in_tiker = keys[curr_from]
        except KeyError:
            errors_log.append(f'[name, time_string, curr_from]\n')
            raise ConvExeption(f'Ошибка при индефикации 1 валюты "{curr_from}"')
        try:
            out_tiker = keys[curr_to]
        except KeyError:
            errors_log.append(f'[name, time_string, curr_to]\n')
            raise ConvExeption(f'Ошибка при индефикации 2 валюты "{curr_to}"')
        try:
            amount = float(amount)
        except KeyError:
            errors_log.append(f'[name, time_string, amount]\n')
            raise ConvExeption(f'Ошибка при индефикации колл-ва указанных едениц{amount}')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={curr_from}&tsyms={curr_to}')
        res = Decimal(json.loads(r.content)[curr_to])
        return res


#r = requests.get(f'http://api.exchangeratesapi.io/v1/latest?access_key=9d75eb30bcbea514fcbbfb2343c49af8')