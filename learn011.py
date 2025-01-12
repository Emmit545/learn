def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 示例使用
num = 7
print(f"The {num}th Fibonacci number is {fibonacci(num)}")
