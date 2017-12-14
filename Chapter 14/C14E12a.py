import itertools
gen = itertools.count(1, 0.5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
gen = itertools.takewhile(lambda n: n < 3,itertools.count(1, 0.5))
print(list(gen))