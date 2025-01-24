"""
默认参数必须指向不变对象
"""
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
