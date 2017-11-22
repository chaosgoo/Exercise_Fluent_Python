symbols = "$@890124"
codes =[]
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

codes = [ord(symbol) for symbol in symbols]
codes = list(filter(lambda c:c>50,map(ord,symbols)))
print(codes)