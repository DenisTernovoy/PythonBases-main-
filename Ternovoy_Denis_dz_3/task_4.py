DATA = {}


def thesaurus_adv(*args):
    global DATA
    for person in args:
        name, surname = person.split()
        global DATA
        if surname[0] not in DATA:
            DATA[surname[0]] = dict()
            if name[0] not in DATA[surname[0]]:
                DATA[surname[0]][name[0]] = []
                DATA[surname[0]][name[0]].append(f'{name} {surname}')
            else:
                DATA[surname[0]][name[0]].append(f'{name} {surname}')
        else:
            if name[0] not in DATA[surname[0]]:
                DATA[surname[0]][name[0]] = []
                DATA[surname[0]][name[0]].append(f'{name} {surname}')
            else:
                DATA[surname[0]][name[0]].append(f'{name} {surname}')
    return sorted(DATA.items())


print(dict(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")))
