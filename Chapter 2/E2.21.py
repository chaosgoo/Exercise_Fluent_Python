import array
numbers = array.array('h',[-2,-1,0,1,2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4 #4->0000 0100 0->0000 0000 
print(numbers)
print(numbers[2])
#1024 -> 0000 0100 0000 0000