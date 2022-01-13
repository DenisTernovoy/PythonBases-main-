src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def generator():
    for i in range(1, len(src), 2):
        if src[i-1] < src[i]:
            yield src[i-1]
            yield src[i]


g = generator()

new_list = [elem for elem in g]
print(new_list)