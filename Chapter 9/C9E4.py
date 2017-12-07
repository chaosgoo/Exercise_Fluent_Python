class Demo:
    @classmethod
    def classmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args

print(Demo.classmeth())
print(Demo.classmeth("spam"))
print(Demo.statmeth())
print(Demo.statmeth("spam"))