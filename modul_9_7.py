def is_prime(func):
    def wrapper(*args,**kwargs):

        result = func(*args,**kwargs)
        if result % 2 == 0:
            simple = result == 2
        else:
            d = 3
            while d ** 2 <= result and result % d != 0:
                d += 2
            simple = d ** 2 > result
        if simple:
            print('Простое число')
        else:
            print('Составное число')
        return result
    return wrapper
@is_prime
def sum_three(*args):
    summ = 0
    for i in args:
       summ += i
    return summ


result = sum_three(2, 3, 6)
print(result)
