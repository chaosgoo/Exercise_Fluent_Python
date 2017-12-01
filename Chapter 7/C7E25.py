import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.time()
            print('start func')
            _result = func(*_args) # 执行位置
            print('end func')
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        print('snooze')
        time.sleep(seconds)

    for i in range(3):
        snooze(0.123)