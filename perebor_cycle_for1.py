x = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
y = input('Введите строку:\n')


for i in x:
    count = 0
    for j in y:
        if i == j:
            count += 1
    if count > 0:
        print('Букв', i, 'в веденной строке', count)
print('Finish')
