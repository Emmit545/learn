"""
题目：统计字符频率
编写一个函数，统计输入字符串中每个字符出现的频率，并按照字母顺序返回结果。
"""
def char_frequency(text):
    # 初始化字典存储字符频率
    frequency = {}
    for char in text:
        if char.isalpha():  # 排除非字母字符
            frequency[char] = frequency.get(char, 0) + 1
    return dict(sorted(frequency.items()))  # 按字母顺序排序

# 测试
text = "hello world"
result = char_frequency(text)
print("字符频率统计：", result)
