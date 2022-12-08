# функция декоратор
import time

def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"время работы: {dt} сек.")
        return res

    return wrapper

@test_time             # второй способ декорирования
def slow_get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

@test_time
def fast_get_nod(a, b):
    if a > b:
        a, b = b, a
        while b:
            a, b = b, a % b
    return a

#slow_get_nod = test_time(slow_get_nod) # первый способ декорирования
#fast_get_nod = test_time(fast_get_nod)
res = slow_get_nod(2, 100000000)
res2 = fast_get_nod(2, 100000000)
print(res, res2)

