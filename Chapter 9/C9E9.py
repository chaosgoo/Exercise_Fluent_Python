from array import array
import math

class Vector2d:
    typecode = "d"

    def __init__(self,x,y):
        self.__x = float(x)
        self.__y = float(y)
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    # C9E8
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __repr__(self):
        class_name = type(self).__name__
        return "{}({!r},{!r})".format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=""):
        # 第一版本
        # components = (format(c, fmt_spec) for c in self)
        # return "({},{})".format(*componets)
        if fmt_spec.endswith("p"):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = "<{}, {}>"
        else:
            coords = self
            outer_fmt = "({}, {})"
        componets = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*componets)

    def angle(self):
        return math.atan2(self.y, self.x)

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))
v1.typecode = "f"
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))
print(Vector2d.typecode)