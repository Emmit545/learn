"""
生成随机密码
"""
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password(12)
print(f"Generated password: {password}")
