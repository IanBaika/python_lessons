def summa(n):
    summa_lambda = lambda n: n+n
    return summa_lambda(n)
some_list = range(1, 1000, 7)
result = map(summa,some_list)
for i in range(0,100):
    print(next(iter(result)))

