"""
def fact(x):
    if x == 1: return 1
    return x*fact(x-1)
print(fact(6))

def fact_it(x):
    res = 1
    for i in range(2, x+1):
        res *= 1
    return res
print(fact_it(6))
def fib_memo(x, cache):
    if x == 0: return 0
    elif x == 1: return 1
    if cache[x] != 0:
        return cache[x]
    cache[x] = fib_memo(x-1, cache) + fib_memo(x-2, cache)
    return cache[x]
cache = [0]*101
print(fib_memo(100, cache))
"""
def func(x, symb):
    if x == 1:
        print(symb*((n-x)//2+1))
        return
    # то что до рекурсивного вызова
    # вызывается на прямом ходу рекурсии
    print(symb*((n-x)//2+1))
    func(x-2,symb)
    # то что после рекурсивного вызова
    # вызывается на обратном ходу рекурсии
    print(symb*((n-x)//2+1))

n = 7
s = '.'
func(n, s)

"""
arr0 = np.array([1,2,3])
arr1 = np.array([4,5,6])
matrix0 = np.stack([arr0, arr1])
print(matrix0**2)

import numpy as np


def lsm(x,y):
    b = ((x*y).mean() - x.mean() * y.mean())/((x**2).mean() - x.mean()**2)
    a = y.mean() - b * x.mean()
    return print("a = ", a,"b = ", b)
x = np.array([1,20,3,4])
y = np.array([2,3,4,19])
lsm(x,y)
"""