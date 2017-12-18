from coro_exc_demo import *
from inspect import getgeneratorstate
exc_coro = demo_exc_handling()
print(next(exc_coro))
print(exc_coro.send(11))
print(exc_coro.send(22))
exc_coro.close()
print(getgeneratorstate(exc_coro))
