"""
将字典按值排序
"""
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))

# 示例使用
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = sort_dict_by_value(my_dict)
print(f"Sorted dictionary: {sorted_dict}")
