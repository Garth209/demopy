"""
Counter 是 collections 模块中的一个类，用于统计可迭代对象中各个元素的出现次数。
"""
from collections import Counter

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
word_count = Counter(words)
print(word_count)  # 输出: Counter({'banana': 3, 'apple': 2, 'orange': 1})
