from sentence import Sentence
s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
    print(word)
print(list(s))
print(s[0])
print(s[5])
print(s[-1])