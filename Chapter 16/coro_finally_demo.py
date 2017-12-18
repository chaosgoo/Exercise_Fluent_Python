class DemoException(Exception):
    """为这次演示定义的异常类型，缺少了这句话就报错"""

def demo_finally():
    print("-> corotine started")
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print("*** DemoException handled. Continuing...")
            else:
                print("-> corotine reveived:{!r}".format(x))
    finally:
        print("-> coroutine ending")
