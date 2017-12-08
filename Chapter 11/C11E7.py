from random import randrange
from C11E4 import Tombola

@Tombola.register
class TombolaList(list):
    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError("pop from empty TomboList")
    
    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))

#Tombola.register(TomboList)