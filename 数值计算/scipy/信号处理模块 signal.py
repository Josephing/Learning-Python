import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt
import random


def 一维卷积运算():
    x = np.array([1,2,3])
    y = np.array([4,5,6])
    print(signal.convolve(x, y)) # 一维卷积运算

# 二维图像卷积
def 二维图像卷积():
    image = misc.ascent() # 二维图像数组，ascent 图像
    w = np.zeros((50, 50)) # 全 0 二维数组，卷积核
    w[0][0] = 1.0 # 修改参数，调整滤波器
    w[49][25] = 1.0
    global image_new
    image_new = signal.fftconvolve(image, w) # 使用 FFT 算法进行卷积

# 高斯模糊
def 高斯模糊():
    image = misc.ascent()  # 二维图像数组，ascent 图像
    w = signal.gaussian(50, 10.0)
    global image_new
    image_new = signal.sepfir2d(image, w, w)

一维卷积运算()
# 二维图像卷积()
高斯模糊()

plt.figure()
plt.imshow(image_new)
plt.gray()
plt.title('Filtered image')
plt.show()

def 中值滤波():
    x = np.arange(0, 100, 10)
    random.shuffle(x) # 打乱顺序
    print(x)
    y = signal.medfilt(x, 3)
    print(y)
中值滤波()