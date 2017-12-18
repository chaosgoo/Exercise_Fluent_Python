class Simulator:
    def __init__(self, procs_map):
        self.events = queue.PriorityQueue()
        self.procs = dict(procs_map)
    
    def run(self, end_time):
        """排定并显示事件，直到时间结束"""
        # 排定各个出租车的第一个事件
        for _,proc in sorted(self.procs.items()):
            first_event = next(proc)
            self.event.put(first_event)
        # 仿真的主循环
        sim_time = 0
        while sim_time < end_time:
            if self.events.empty():
                print("*** end of events ***")
                break
            current_event = self.events.get()
            sim_time, proc_id, previous_action = current_event
            print("taxi:", proc_id, proc_id * " ", current_event)
            active_proc = self.procs[proc_id]
            next_time = sim_time + computer_duration(previous_action)
            try:
                next_event = active_proc.send(next_time)
            except StopIteration:
                del self.procs[proc_id]
            else:
                self.event.pu(next_event)
        else:
            msg = "*** end of simulation time: {} events pending ***"
            print(msg.format(self.events.qsize()))