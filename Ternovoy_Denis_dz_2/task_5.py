prices = [57.8, 46.51, 97, 84, 2.40, 3.04, 10.28, 18.46, 29.99, 99.90, 84.90]
list_printed = []

for i in range(len(prices)):
    price = ''
    rubles = int(prices[i])
    cents = int(round(prices[i] - rubles, 2) * 100)
    list_printed.append(f'{rubles} руб {cents:02} коп')
print(*list_printed, sep =', ')


list_printed = []
for i in range(len(prices)):
    price = ''
    rubles = int(sorted(prices)[i])
    cents = int(round(sorted(prices)[i] - rubles, 2) * 100)
    list_printed.append(f'{rubles} руб {cents:02} коп')
print(*list_printed, sep =', ')
print()

prices_sorted = sorted(prices, reverse=True)
list_printed = []
for i in range(5):
    price = ''
    rubles = int(prices_sorted[i])
    cents = int(round(prices_sorted[i] - rubles, 2) * 100)
    list_printed.append(f'{rubles} руб {cents:02} коп')
print(*list_printed, sep=', ')