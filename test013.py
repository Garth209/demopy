"""
统计一段文本中的单词数量
"""
def word_count(text):
    words = text.split()
    return len(words)

# 示例使用
text = "Python is an amazing programming language."
print("Word count:", word_count(text))
