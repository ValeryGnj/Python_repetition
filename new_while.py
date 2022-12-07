x = ''

while len(x) < 5:
    y = input('ввод данных: ')
    if y == 'o':
        continue
    if y == 'l':
        break
    x += y
else:
    print(x)
print('программа работает дальше: ')
