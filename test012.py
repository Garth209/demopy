"""
判断一个字符串是否是回文
"""
def is_palindrome(s):
    return s == s[::-1]

# 示例使用
word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")
