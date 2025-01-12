"""
计算斐波那契数列的第 n 个数。斐波那契数列的定义是：F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
"""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 示例使用
num = 7
print(f"The {num}th Fibonacci number is {fibonacci(num)}")
