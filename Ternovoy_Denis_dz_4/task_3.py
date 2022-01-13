<<<<<<< HEAD
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Костя', 'Станислав'
]

classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generator():
    for i in range(len(tutors)):
        try:
            yield tutors[i], classes[i]
        except Exception:
            yield tutors[i], None


g = generator()
print(g)

for elem in g:
    print(elem)

=======
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
        return money
    except Exception:
        return


print(f'USD - {currency_rates("USD")}, {current_date}')
print(f'EUR - {currency_rates("EUR")}, {current_date}')


code = input().upper()
print(f'{code} - {currency_rates(code)}')

>>>>>>> DZ_4
