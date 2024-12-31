"""
题目：单词反转
编写一个函数，接收一个句子作为输入，将句子中的每个单词反转，但单词的顺序保持不变。
"""
def reverse_words(sentence):
    # 在这里实现你的逻辑
    return " ".join([word[::-1] for word in sentence.split()])

# 测试
sentence = "Hello world Python is fun"
result = reverse_words(sentence)
print("反转后的句子：", result)
