import random


def get_jokes(n, answer):
    """

    В случае answer == '+' при помощи модуля random n-раз создаются строки, состоящие из 3-х слов:
    по одному из каждой коллекции.

    В случае answer == '-' создаются копии исходных коллекций для того чтобы удалять использованные в коде
    элементы, не затрагивая оригинальные словари.

    Полученные строки сохраняются в список my_jokes, который возвращается пользователю.
    """


    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    my_jokes = []

    nouns_1 = nouns.copy()
    adverbs_1 = adverbs.copy()
    adjectives_1 = adjectives.copy()

    for i in range(n):
        if answer == '+':
            joke = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
            my_jokes.append(joke.capitalize())
        else:
            noun = random.choice(nouns_1)
            adverb = random.choice(adverbs_1)
            adjective = random.choice(adjectives_1)

            joke = f'{noun} {adverb} {adjective}'

            del nouns_1[nouns_1.index(noun)]
            del adverbs_1[adverbs_1.index(adverb)]
            del adjectives_1[adjectives_1.index(adjective)]

            my_jokes.append(joke.capitalize())

    return my_jokes


request = input('Желаете, чтобы слова в шутках повторялись? (+\-)\n')
print(get_jokes(n = int(input('Сколько шуток Вы хотите?\n')), answer = request))
