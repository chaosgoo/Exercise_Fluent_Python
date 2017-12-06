import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None) #与书中不同，我的结果是True,但是在控制台中确实已经变成了Noe
print(wref() is None)