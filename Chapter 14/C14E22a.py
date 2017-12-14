def chain_v1(*iterables):
    for it in iterables:
        for i in it:
            yield i

s = "ABC"
t = tuple(range(3))
print(list(chain_v1(s, t)))

def chain_v2(*iterables):
    for i in iterables:
        yield from i

print(list(chain_v2(s,t)))