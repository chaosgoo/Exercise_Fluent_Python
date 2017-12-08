from C11E4 import Tombola
from C11E7 import TombolaList

print(issubclass(TombolaList,Tombola))
t = TombolaList(range(100))
print(isinstance(t,Tombola))