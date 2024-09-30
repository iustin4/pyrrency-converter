#!/usr/bin/env python3

import os
import requests
import argparse
from dotenv import load_dotenv, dotenv_values

load_dotenv()

base_url = f'https://api.freecurrencyapi.com/v1/latest?apikey={os.getenv('API_KEY')}'

def convert(base_currency, currency, amount):
    base_currency = str(base_currency).capitalize()
    currency = str(currency).capitalize()
    if(requests.get(f'{base_url}&currencies={currency}&base_currency={base_currency}').status_code != 200):
        return print('Invalid currency!')
    json = requests.get(f'{base_url}&currencies={currency}&base_currency={base_currency}').json()['data']
    print(round((json.get(currency) * amount), 3))

def main():
    parser = argparse.ArgumentParser(description='Currency Converter CLI')

    parser.add_argument('base_currency', type=str, help='The currency to convert from')
    parser.add_argument('target_currency', type=str, help='The currency to convert to')
    parser.add_argument('amount', type=float, help='The amount to convert')

    args = parser.parse_args()

    convert(args.base_currency, args.target_currency, args.amount)

if __name__ == '__main__':
    main()