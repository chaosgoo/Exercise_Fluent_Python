from coro_exc_demo import *
from inspect import getcoroutinestate

exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.throw(ZeroDivisionError))
print(getcoroutinestate(exc_coro))