"""
生成杨辉三角
"""
def generate_pascals_triangle(n):
    if n <= 0:
        return []
    
    triangle = [[1]]  # 第一个元素是 [1]
    
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # 每行开头是 1
        # 生成当前行中间的数字
        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)  # 每行结尾是 1
        triangle.append(new_row)
    
    return triangle

# 测试
n = 5
result = generate_pascals_triangle(n)
for row in result:
    print(row)
