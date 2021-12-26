### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = int(input())

days = duration // 86400
duration = duration % 86400
hours = duration // 3600
duration = duration % 3600
minutes = duration // 60
duration = duration % 3600
seconds = duration % 60

if days != 0:
    print(days, 'дн', end = ' ')
    print(hours, 'час', end=' ')
    print(minutes, 'мин', end=' ')
    print(seconds, 'сек')
elif days == 0 and hours != 0:
    print(hours, 'час', end=' ')
    print(minutes, 'мин', end=' ')
    print(seconds, 'сек')
elif hours == 0 and minutes > 0:
    print(minutes, 'мин', end=' ')
    print(seconds, 'сек')
else:
    print(seconds, 'сек')