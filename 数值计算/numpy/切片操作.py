import numpy as np

a = np.arange(10)
print(a)
print(a[::-1]) # 反向切片
print(a[::2]) # 隔一个取一个元素
print(a[:5]) # 前 5 个元素

print("-------------")

c = np.arange(25)
c.shape = (5,5)
print(c)
print(c[0,2:5]) # 第 0 行中下标 [2,5）之间的元素值
print(c[1]) # 第 1 行中所有的元素
print(c[2:5,2:5]) #行下标和列下标都介于 [2,5）之间的元素值