for n in range(1, 101):
    if n % 10 == 1 and (n > 20 or n < 10):
        print(n, 'процент')
    elif n % 10 in [2,3,4] and (n > 20 or n < 10):
        print(n, 'процента')
    else:
        print(n, 'процентов')