# 不能直接导入E5.1 因为文件名称不符合规范...sad
def factorial(n):
    '''returns n'''
    return 1 if n < 2 else n * factorial(n-1)

fact = factorial
print(fact)
print(fact(5))
print(map(fact,range(11)))
print(list(map(fact,range(11))))