"""
计算圆的面积
"""
import math

def circle_area(radius):
    return math.pi * radius**2

# 示例使用
radius = 5
print(f"The area of the circle with radius {radius} is {circle_area(radius):.2f}")
