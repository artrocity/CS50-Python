import requests
import sys
import json

def is_number(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

y = sys.argv
#User inputs CLI for number of Bitcoins, if != float, exit
try:
    if len(y) != 2:
        sys.exit(1)

    x = y[1]

    if not is_number(x):
        sys.exit(1)

    #query API CoinDesk Bitcoin Price Index, get cli input, store json value
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin = response.json()

    #return JSON nested key of current bitcoin as float
    rate = bitcoin["bpi"]["USD"]["rate_float"]
    x = float(x) * float(rate)
    #output costs of Bitcoin in 4 decimal places using , as sep
    print(f"${x:,.4f}")
except (ValueError, requests.RequestException, KeyError) as e:
    print("Error:", e)