import random
from Tombola import Tombola

class BingoCage(Tombola):

    @classmethod
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    @classmethod
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
    
    @classmethod
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")
    
    @classmethod
    def __call__(self):
        self.pick()