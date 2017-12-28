import numpy as np

x = np.array((1,2,3))
print(x+2) # 数组与数值相加
print(x*2) # 数组与数值相乘
print(x**3) # 数组的数值幂
print(x/2) # 数组与数值相除
print(x//2) # 数组与数值整除
print(x%2) # 数组与数值余数

print("------------")

y = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(x*y) # 数组与数组相乘（注：不是矩阵相乘）
print(x*y/y) # 数组间除法
print(x*y/x)
print(x+x) # 数组间加法
print(x*x) # 数组间乘法
print(x-x)# 数组间减法
print(x/x)# 数组间除法