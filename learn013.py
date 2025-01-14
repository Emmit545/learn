"""
统计列表中偶数和奇数的数量
"""
def count_even_odd(numbers):
    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = len(numbers) - even_count
    return even_count, odd_count

# 示例使用
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens, odds = count_even_odd(nums)
print(f"Evens: {evens}, Odds: {odds}")
