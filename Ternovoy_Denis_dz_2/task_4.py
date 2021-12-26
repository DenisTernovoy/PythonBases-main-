list_staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(list_staff)):
    name = ''
    for j in range(1, len(list_staff[i])):
        name = name + list_staff[i][-j]
        if list_staff[i][-j] == ' ':
            break
    name = name[::-1].strip()
    print('Привет,', name.capitalize() + '!')