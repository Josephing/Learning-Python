import math
print(math.factorial(10)) # 计算阶乘

from decimal import *
print(1.0/ 81)

getcontext().prec = 100 # 设置 decimal 模块的精度为小数点后 100 位
print(Decimal(1)/Decimal(81))