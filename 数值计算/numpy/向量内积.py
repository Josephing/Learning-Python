import numpy as np

a = np.array((5,6,7))
b = np.array((6,6,6))
c = np.array(([1,2,3],[4,5,6],[7,8,9]))

print(a.dot(b)) # 向量内积
print(np.dot(a,b))

cT = c.T # 转置

print(c.dot(a)) # 二维数组的每行与一维向量计算内积
print(c[0].dot(a)) # 两个一维向量计算内积
print(c[1].dot(a))
print(c[2].dot(a))

print(a.dot(c)) # 一维向量与二维向量的每列计算内积

print(a.dot(cT[0]))
print(a.dot(cT[1]))
print(a.dot(cT[2]))
