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

