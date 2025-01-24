"""
递归-阶乘
"""
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
