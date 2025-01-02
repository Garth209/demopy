"""
实现一个加权的随机选择
"""
import random

class WeightedRandomPicker:

    def __init__(self, elements: list, weights: list):
        self.elements = elements
        self.prefix_sums = []
        
        # 计算前缀和数组
        prefix_sum = 0
        for weight in weights:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        
        self.total_weight = prefix_sum

    def pick(self) -> str:
        # 生成一个随机数，范围在 [1, total_weight] 之间
        rand_value = random.randint(1, self.total_weight)
        
        # 二分查找前缀和数组，找到对应的元素
        left, right = 0, len(self.prefix_sums) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.prefix_sums[mid] < rand_value:
                left = mid + 1
            else:
                right = mid - 1
        
        return self.elements[left]

# 测试代码
picker = WeightedRandomPicker(["a", "b", "c"], [1, 2, 3])
p
