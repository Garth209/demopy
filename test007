from collections import Counter

def most_common_element(lst):
    # 使用 Counter 统计元素出现的频率
    count = Counter(lst)
    
    # 找到出现次数最多的元素
    most_common = count.most_common(1)[0]
    
    return most_common[0]  # 返回出现次数最多的元素

# 示例使用
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
result = most_common_element(lst)
print(result)
