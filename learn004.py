"""
合并两个已排序的列表并返回一个新的排序列表
"""
def merge_sorted_lists(list1, list2):
    # 使用两个指针，分别遍历两个列表
    merged_list = []
    i, j = 0, 0
    
    # 遍历直到一个列表用尽
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # 处理剩余的元素
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

# 示例使用
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = merge_sorted_lists(list1, list2)
print(f"合并后的排序列表: {result}")
