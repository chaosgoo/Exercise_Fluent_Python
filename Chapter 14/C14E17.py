import itertools

print(list(itertools.chain(enumerate("ABC"))))
print(list(itertools.chain.from_iterable(enumerate("ABC"))))
print(list(zip("ABC",range(5))))
print(list(zip("ABC",range(5),[10,20,30,40])))
print(list(itertools.zip_longest("ABC",range(5))))
print(list(itertools.zip_longest("ABC",range(5),fillvalue="?")))
