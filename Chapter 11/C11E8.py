from Tombola import Tombola
from TombolaList import TombolaList

print(issubclass(TombolaList,Tombola))
t = TombolaList(range(100))
print(isinstance(t,Tombola))