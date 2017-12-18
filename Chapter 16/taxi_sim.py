from collections import namedtuple
Event = namedtuple("Event","time proc action")
def taxi_process(ident, trips, start_time=0):
    """每次改变状态时创建时间，把控制权让给仿真器"""
    time = yield Event(start_time, ident, "leave garage")
    for i in  range(trips):
        time = yield Event(time, ident, "pick up passenger")
        time = yield Event(time, ident, "drop off passenger")
    yield Event(time, ident, "going home")
    # 出租车进程结束
