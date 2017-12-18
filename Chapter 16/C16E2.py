from inspect import getgeneratorstate

def simple_coro2(a):
    print("-> Started: a=", a)
    b = yield a
    print("-> Received: b=", b)
    c = yield a + b
    print("-> Reveivec: c=", c)

my_coro2 = simple_coro2(14)
print(getgeneratorstate(my_coro2))
print(next(my_coro2))
print(getgeneratorstate(my_coro2))
print(my_coro2.send(28))
try:
    print(my_coro2.send(99))
finally:
    print(getgeneratorstate(my_coro2))