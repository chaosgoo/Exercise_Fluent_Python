from arithmeticProgression import ArithmeticProgression
from fractions import Fraction
from decimal import Decimal

ap = ArithmeticProgression(0, 1, 3)
print(list(ap))
ap = ArithmeticProgression(1, 0.5, 3)
print(list(ap))
ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap))
ap = ArithmeticProgression(0, Fraction(1,3), 1)
# Fraction 分数
print(list(ap))
ap = ArithmeticProgression(0, Decimal(".1"), 0.3)
print(list(ap))