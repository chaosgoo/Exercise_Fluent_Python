from coroaverage0 import *

coro_avg = averager()
print(next(coro_avg))
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))