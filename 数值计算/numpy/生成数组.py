import numpy as np

# 将列表转换为数组
a1 = np.array((1,2,3,4,5))
print(a1)

# 将 range 对象转为数组
a2 = np.array(range(5))
print(a2)

a3 = np.array([[1,2,3],[4,5,6]])
print(a3)

# 生成等差数组
a4 = np.linspace(0,10,11)
print(a4)

# 对数数组
a5 = np.logspace(0,100,10)
print(a5)

# 全 0 数组
a6 = np.zeros((3,1))
a7 = np.zeros((1,3))
print(a6)
print(a7)

# 全 1 数组
a8 = np.ones((3,2))
print(a8)

# 单位矩阵
a9 = np.identity(3)
print(a9)

# 空数组，只申请空间而不初始化，元素值不确定
a10 = np.empty((2,3))
print(a10)