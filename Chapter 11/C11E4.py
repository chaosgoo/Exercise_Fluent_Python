import abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """从可迭代对象中添加元素的"""
    
    @abc.abstractmethod
    def pick(self):
        """随机删除元素,然后返回"""
        """如果实例为空，则抛出“LookupError"""
    
    def loaded(self):
        """如果至少有一个元素，就返回True，否则返回False"""

    def inspect(self):
        """返回一个有序元组，由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))