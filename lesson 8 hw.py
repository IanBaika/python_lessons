some_list = range(1, 1000, 7)
result = map(lambda n: n*2,some_list)
for i in range(0,100):
    print(next(iter(result)))


