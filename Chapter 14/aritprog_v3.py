import itertools

def arritprog_gen(begin, step, end=None):
    first = type(begin+step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambad n: n < end,ap_gen)
    return ap_gen