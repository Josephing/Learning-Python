import numpy as np

# 求积分
from scipy.integrate import quad,dblquad,nquad

# 一维积分
print(quad(lambda x:np.exp(-x),0,np.inf)) # 构造函数：e^-x，积分区间：[0,+∞]，返回结果第一个为积分的值，第二个为误差范围

# 二维积分
print(dblquad(lambda t,x:np.exp(-x*t)/t**3,0,np.inf,lambda x:1,lambda x:np.inf)) # 二元积分，t的范围为常数，x的范围是t的函数

# n 维积分
def f(x,y):
    return x**y
def bound_y():
    return [0,0.5] # y的边界，即x的范围
def bound_x(y):
    return [0,1-2*y] # x的边界，即y的范围
print(nquad(f,[bound_x,bound_y]))