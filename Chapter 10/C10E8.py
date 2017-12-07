import functools
import operator
n = 0
for i in range(1, 6):
    n ^= i

print(n)

print(functools.reduce(lambda a, b: a^b, range(6)))
print(functools.reduce(operator.xor, range(6)))
