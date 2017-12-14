from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools
class Vector:
    typecode = "d"
    shortcut_names = "xyzt"
    # components 成分 
    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("["):-1]
        return "Vector({})".format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + 
                bytes(self._components))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return len(self) == len(other)
        else:
            return NotImplemented
        # return len(self) == self(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = "{.__name__!r} object has no arrtibute {!r}"
        raise AttributeError(msg.format(cls, name))
    
    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("h"):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],self.angles())
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt ="({})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(", ".join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n*scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    def __matmul__(self, other):
        try:
            return sum(a * b for a,b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other

    def __ne__(self, other):
        eq_result = self == other
        if eq_result is NotImplemented:
            return NotImplemented
        else:
            return not eq_result
        
