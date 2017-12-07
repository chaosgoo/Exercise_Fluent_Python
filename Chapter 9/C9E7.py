class Vector2d:
      # C9E9
    __slots__ = ("__x", "__y")
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

  