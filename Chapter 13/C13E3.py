from Vector import Vector

v1 = Vector([3, 4, 5])
v2 = Vector([6, 7, 8])

print(v1 + v2)
print(v1 + v2 == Vector([3+6, 4+7, 5+8]))
v1 = Vector([3, 4, 5, 6])
v3 = Vector([1, 2])
print(v1 + v3)