def make_averger():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager
# C7E10
avg = make_averger()
print(avg(10))
print(avg(11))
print(avg(12))
# C7E11
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
# C7E12
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)