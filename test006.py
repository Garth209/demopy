def is_palindrome(x):
    # 负数和末尾为 0 的数不能是回文数
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        # 获取当前数字的最后一位
        reversed_half = reversed_half * 10 + x % 10
        x //= 10  # 移除最后一位数字
    
    # 判断是否是回文数（奇数长度时需要判断除去中间数字后是否相等）
    return x == reversed_half or x == reversed_half // 10

# 示例使用
x1 = 121
x2 = -121
x3 = 10

print(f"{x1} 是回文数吗？ {is_palindrome(x1)}")
print(f"{x2} 是回文数吗？ {is_palindrome(x2)}")
print(f"{x3} 是回文数吗？ {is_palindrome(x3)}")
