import numpy as np

a = np.arange(1,11,1)
print(a)

a.shape = (2,5)
print(a)

a.shape = (5,-1) # -1 表示自动计算
print(a)

b = a.reshape(2,5) # reshape 方法返回新数组
print(b)