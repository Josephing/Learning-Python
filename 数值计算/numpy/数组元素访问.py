import numpy as np

y = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(y)

print(y[0])
print(y[0][0])

x = np.arange(0, 100, 10, dtype=np.floating ) # 创建等差数组
print(x)

index = np.random.randint(0,len(x),5) # 生成 5 个随机整数作为下标
print(index)
print(x[index])

x[index] = [1,2,3,4,5] # 同时修改多个下标指定的元素值
print(x)

x[[1,2,3]] # 同时访问多个元素的值