from FrenchDeck2 import *
import io

def print_mro(cls):
    print(", ".join(c.__name__ for c in cls.__mro__))
if __name__ == "__main__":
    print(bool.__mro__)
    print_mro(bool)
    print_mro(FrenchDeck2)
    print_mro(io.BytesIO)
    print_mro(io.TextIOWrapper)
