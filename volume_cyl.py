import math

PI = math.pi

def radius():
    d = float(input('Введите радиус в сантиметрах:  '))
    d /= 2
    return d

def hight():
    h = float(input('Введите высоту в сантиметрах:  '))
    return h

def volume():
    r = radius()
    y = hight()
    s = PI*r**2
    v = s*y
    return v
#print('Объем цилиндра равно', volume(), 'см3')

def mass(g):
    n = float(input('Плотность г/см3:  '))
    return g*n/1000
print('Вес цилиндра в кг', mass(volume()))
