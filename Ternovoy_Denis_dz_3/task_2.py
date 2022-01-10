def num_translate(word):

    MY_DICT = {
        'one': 'Один',
        'two': 'Два',
        'three': 'Три',
        'four': 'Четыре',
        'five': 'Пять',
        'six': 'Шесть',
        'seven': 'Семь',
        'eight': 'Восемь',
        'nine': 'Девять',
        'ten': 'Десять'
    }

    if word.islower():
        return MY_DICT.get(word.lower()).lower()
    else:
        return MY_DICT.get(word.lower())


print(num_translate(input()))