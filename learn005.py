"""
找出两个列表的交集
"""
def intersection(list1, list2):
    # 使用集合去除重复元素，并求交集
    return list(set(list1) & set(list2))

# 示例使用
list1 = [1, 2, 2, 1]
list2 = [2, 2]

result = intersection(list1, list2)
print(f"交集: {result}")
