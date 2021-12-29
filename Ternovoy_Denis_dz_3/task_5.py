import random


def get_jokes(number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    my_jokes = []
    for i in range(number):
        joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        my_jokes.append(joke.capitalize())
    return my_jokes


print(get_jokes(int(input('Сколько шуток Вы хотите?\n'))))
