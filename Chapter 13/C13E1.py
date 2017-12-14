import decimal

ctx = decimal.getcontext()
ctx.prec = 40
one_thrid = decimal.Decimal("1") / decimal.Decimal("3")
print(one_thrid)
print(one_thrid == +one_thrid)
ctx.prec = 28
print(one_thrid == +one_thrid)
print(+one_thrid)
