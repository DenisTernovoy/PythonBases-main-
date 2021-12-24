#Задание 2 (А)

numbers = [int(i**3) for i in range(1,1001,2)]
sum_numbers = 0

for n in numbers:
    temp = 0
    number = n
    while n != 0:
        last_digit = n % 10
        temp += last_digit
        n = n // 10
    if temp % 7 == 0:
        sum_numbers += number

print('Ответ(А): ', sum_numbers)

#Задание 2 (Б)

sum_numbers = 0
for i in range(len(numbers)):
    temp = 0
    number = numbers[i] + 17
    while number != 0:
        last_digit = number % 10
        temp += last_digit
        number = number // 10
    if temp % 7 == 0:
        sum_numbers += numbers[i] + 17

print('Ответ(Б): ', sum_numbers)