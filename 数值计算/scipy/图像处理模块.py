from scipy import misc, ndimage
import matplotlib.pyplot as plt
import numpy as np

def 图像滤波():
    # 原始图像
    face = misc.face() # face 是测试图像之一
    plt.figure() # 创建图像
    plt.imshow(face) # 绘制测试图像
    plt.show()

    # 高斯滤波
    blurred_face1 = ndimage.gaussian_filter(face, sigma=7)
    plt.imshow(blurred_face1)
    plt.show()

    # 边缘锐化
    blurred_face2 = ndimage.gaussian_filter(face, sigma=1)
    blurred_face3 = ndimage.gaussian_filter(face, sigma=3)
    sharp_face = blurred_face3 + 6 * (blurred_face3 - blurred_face1)
    plt.imshow(sharp_face)
    plt.show()

    # 中值滤波
    median_face = ndimage.median_filter(face, 7)
    plt.imshow(median_face)
    plt.show()

def 数学形态学():
    square = np.zeros((32, 32))
    square[10:20, 10:20] = 1 # 把其中一部分设为 1
    x,y = (32 * np.random.random((2,15))).astype(np.int) # 生成一些随机位置
    square[x,y] = 1 # 把随机位置设为 1
    plt.imshow(square)
    plt.show()

    open_square = ndimage.binary_opening(square) # 开运算
    plt.imshow(open_square)
    plt.show()

    eroded_square = ndimage.binary_erosion(square) # 膨胀运算
    plt.imshow(eroded_square)
    plt.show()

    closed_square = ndimage.binary_closing(square) # 闭运算
    plt.imshow(closed_square)
    plt.show()

图像滤波()
数学形态学()