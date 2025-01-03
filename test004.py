def reverse_and_check_palindrome(s):
    # 反转字符串
    reversed_s = s[::-1]
    
    # 判断是否为回文
    is_palindrome = (s == reversed_s)
    
    return reversed_s, is_palindrome

# 示例使用
s1 = "racecar"
s2 = "hello"

reversed_s1, is_palindrome1 = reverse_and_check_palindrome(s1)
reversed_s2, is_palindrome2 = reverse_and_check_palindrome(s2)

print(f"字符串: {s1}, 反转后: {reversed_s1}, 是否为回文: {is_palindrome1}")
print(f"字符串: {s2}, 反转后: {reversed_s2}, 是否为回文: {is_palindrome2}")
