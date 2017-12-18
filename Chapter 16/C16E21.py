from taxi_sim import taxi_process
taxi = taxi_process(ident=13,trips=2,start_time=0)
time = 0
print(next(taxi))
# 不知道如何在这里调用_.time,所以只能用其他变量去替代了
print(taxi.send(time+7))
time += 7
print(taxi.send(time+23))
time += 23
print(taxi.send(time+5))
time += 5
print(taxi.send(time+48))
time += 48
print(taxi.send(time+1))
time += 1
print(taxi.send(time+10))
time += 10