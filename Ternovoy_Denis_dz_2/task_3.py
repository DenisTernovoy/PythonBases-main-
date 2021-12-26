list_phrase = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i in range(len(list_phrase)):
    if list_phrase[i].isdigit():
        list_phrase[i] = f'"{int(list_phrase[i]):02}"'
    elif list_phrase[i].startswith('+'):
        list_phrase[i] = f'"+{int(list_phrase[i][1:]):02}"'
print(*list_phrase)