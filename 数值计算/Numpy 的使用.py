#enconding=utf-8

import numpy as np # 导入 numpy 模块并去别名为 np

# 查看数组属性
np_lst=np.array([[1,2,3],[4,5,6]],dtype=float)
print(type(np_lst))  # 输出数组的数据结构
print(np_lst.dtype)  # 输出数组元素的数据类型
print(np_lst.shape) # 输出数组几行几列
print(np_lst.ndim)  # 输出数组的维数
print(np_lst.itemsize)  # 输出数组每个元素的大小（单位为字节，float64为64位，即8字节）
print(np_lst.size)  # 输出数组有几个元素

# 全0数组、全1数组、单位矩阵
print(np.zeros([2,4]))  # 输出 2 行 4 列的 全0数组
print(np.ones([3,5]))  # 输出 3 行 5 列的 全1数组
print(np.eye(3)) # 输出一个单位矩阵    

# 随机数 random
print(np.random.rand())  # 输出 1 个 [0-1] 间的随机数
print(np.random.rand(2,4))  # 输出 2 行 4 列 [0-1] 间均匀分布的随机数 组成的数组
print(np.random.randint(1,10))  # 输出 1 个 [1-10] 间的随机整数
print(np.random.randint(1,10,3))  # 输出 3 个 [1-10] 间的随机整数
print(np.random.randn())  # 输出 1 个标准正态分布的随机数
print(np.random.randn(2,4))  # 输出 2 行 4 列 的标准正态分布的随机数 组成的数组
print(np.random.choice([10,2,30]))  # 从 10，2，30 中随机选出一个数
print(np.random.beta(1, 10, 8))  # 输出 8 个 [1,10] 间 β 分布的数

# 等差数列 arange 与数组变形 reshape
print(np.arange(1,11))  # 输出 [1,11) 间的 int 型等差数列
print(np.arange(1,11).reshape([2,5]))  # 输出 [1,11) 间的 int 型等差数列，并将其转为 2 行 5 列
print(np.arange(1,11).reshape([2,-1]))  # 输出 [1,11) 间的 int 型等差数列，并将其转为 2 行 y 列（y 根据数列长度和行数自动确定）
print(np.arange(1,11).reshape([-1,5]))  # 输出 [1,11) 间的 int 型等差数列，并将其转为 x 行 5 列（x 根据数列长度和列数自动确定）

# 基本数学运算
lst1 = np.arange(1,11).reshape([2,5])
print(np.exp(lst1))  # 对 lst 中每个元素求 自然指数
print(np.exp2(lst1)) # 对 lst 中每个元素求 自然指数的平方
print(np.sqrt(lst1)) # 对 lst 中每个元素求 开方
print(np.sin(lst1)) # 对 lst 中每个元素求 sin
print(np.log(lst1)) # 对 lst 中每个元素求 对数（以e为底数）

# 数组的轴运算
lst2 = np.array( [ [[1,2,3,4],[4,5,6,7]], [[7,8,9,10],[10,11,12,13]] , [[14,15,16,17],[18,19,20,21]] ] )
print(lst2.sum())   # 求 lst2 中所有元素的和
print(lst2.sum(axis=0)) # axis 为轴
print(lst2.max())
print(lst2.max(axis=0)) #
print(lst2.min())

# 两个数组的运算
lst1 =np.array([10,20,30,40])
lst2 =np.array([4,3,2,1])
print(lst1 + lst2) # 对 lst1 与lst2 进行加法运算
print(lst1 - lst2) # 对 lst1 与lst2 进行减法运算
print(lst1 * lst2) # 对 lst1 与lst2 进行乘法运算
print(lst1 / lst2) # 对 lst1 与lst2 进行除法运算
print(lst1 ** 2) # 对 lst1 与lst2 进行幂运算
print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2]))) # 对 lst1 与lst2 进行点乘运算
print(np.concatenate((lst1,lst2),axis=0)) # 将 lst2 追加到 lst1 后面去（合成一个一维数组）
print(np.vstack((lst1,lst2))) # 等价于：np.concatenate(tup, axis=0)
print(np.hstack((lst1,lst2))) # 等价于：np.concatenate(tup, axis=1)
print(np.dstack((lst1,lst2))) # 等价于：np.concatenate(tup, axis=2)
print(np.split(lst1,2)) # 将 lst1 分为两份


# 求矩阵的逆、转置、行列式、特征值、特征向量                                                                                                        
from numpy.linalg import *                      
                                                                                                          
lst = np.array( [[1,2],[3,4]] )                 
print(inv(lst)) # 求矩阵 lst 的逆矩阵                  
print(lst.transpose()) # 求矩阵 lst 的转置矩阵          
print(det(lst)) # 求矩阵 lst 的行列式                  
print(eig(lst)) # 求矩阵 lst 的特征值和特征向量，第一个 array 是特征值，第二个 array 是特征向量
                                                
# 解方程                                           
lst1 = np.array( [[1,2],[3,4]] )                
result = np.array([[5],[7]])                    
print(solve(lst,result)) # 解方程组 1x+2y=5 ；3x+4y=8
                                                
# 生成一元多次方程组                                     
print(np.poly1d([6,8,3])) # 生成 6x^2 + 8x + 3    