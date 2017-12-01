class Averager():

    def __init__(self):
        self.serise = []
    
    def __call__(self, new_value):
        self.serise.append(new_value)
        total = sum(self.serise)
        return total / len(self.serise)

avg = Averager()

print(avg(10))
