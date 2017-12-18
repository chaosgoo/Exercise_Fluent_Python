from coroaverage1 import averager

coro_avg = averager()
print(coro_avg.send(40))
print(coro_avg.send(50))
try:
    print(coro_avg.send("spam"))
except TypeError as e:
    print(e)
finally:
    print(coro_avg.send(60)) #携程已经终止 所以会抛出StopIteration异常
