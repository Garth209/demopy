def fibonacci(n):
    # 使用两个变量记录斐波那契数列的前两个数
    a, b = 0, 1
    
    # 使用循环计算从 2 到 n 的斐波那契数
    for _ in range(n):
        a, b = b, a + b
    
    return a

# 示例使用
n = 6
result = fibonacci(n)
print(f"斐波那契数列的第 {n} 项: {result}")
