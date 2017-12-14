from AddableBingoCage import AddableBingoCage
vowels = "AEIOU"
globe = AddableBingoCage(vowels)
print(globe.inspect())
print(globe.pick() in vowels)
print(len(globe.inspect()))
globe2 = AddableBingoCage("XYZ")
globe3 = globe + globe2
print(len(globe3.inspect()))
print(globe3.inspect())
# void = globe + [10, 20]
globe_orig = globe
print(len(globe.inspect()))
globe += globe2
print(len(globe.inspect()))
globe += ['M', 'N']
print(len(globe.inspect()))
print(globe is globe_orig)
# globe += 1
