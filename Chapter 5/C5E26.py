from operator import mul
from functools import partial
triple = partial(mul,3)
print(triple(7))

ls = list(map(triple,range(1,10)))

print(ls)