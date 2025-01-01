def single_number(nums):
    result = 0
    for num in nums:
        result ^= num  # 异或运算
    return result

# 测试
print(single_number([4, 1, 2, 1, 2]))  # 4
print(single_number([2, 2, 1]))        # 1
print(single_number([1]))             # 1
