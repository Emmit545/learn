def count_letters_and_digits(s):
    letter_count = 0
    digit_count = 0
    
    # 遍历字符串中的每个字符
    for char in s:
        if char.isalpha():  # 判断是否是字母
            letter_count += 1
        elif char.isdigit():  # 判断是否是数字
            digit_count += 1
    
    return letter_count, digit_count

# 示例使用
s = "Hello123 World!@#"
letters, digits = count_letters_and_digits(s)
print(f"字母个数: {letters}")
print(f"数字个数: {digits}")
