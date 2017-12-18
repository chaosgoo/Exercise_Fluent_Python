def simple_coroutine():
    print("-> coroutine started")
    x = yield
    print("-> coroutine received:", x)

my_coro = simple_coroutine()
print(my_coro)
next(my_coro) #预激
# my_coro.send(42)
my_coro = simple_coroutine()
my_coro.send(1729)