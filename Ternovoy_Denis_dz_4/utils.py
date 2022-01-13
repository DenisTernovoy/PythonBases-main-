import requests
import datetime as dt
from decimal import Decimal as D


def currency_rates(code):
    global current_date

    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")

    response.encoding = 'utf-8'
    text = response.text
    day = text[text.find("Date=") + 6:text.find("Date=") + 16].replace('.','')
    current_date = dt.date(day=int(day[:2]), month=int(day[2:4]), year=int(day[4:]))
    try:
        index = text.find(code)
        index_value = text[index:].find("Value")
        money = D(text[index:][index_value + 6:index_value + 12].replace(',', '.'))
        return f'{money}, {current_date}'
    except Exception:
        return


if __name__ == '__main__':
    import sys

    exit(currency_rates(sys.argv))