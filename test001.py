def reverse_words(sentence):
    # 在这里实现你的逻辑
    return " ".join([word[::-1] for word in sentence.split()])

# 测试
sentence = "Hello world Python is fun"
result = reverse_words(sentence)
print("反转后的句子：", result)
