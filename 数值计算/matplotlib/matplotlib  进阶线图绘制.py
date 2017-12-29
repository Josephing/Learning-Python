import numpy as np
import matplotlib.pyplot as plt

# 绘制 散点图
fig = plt.figure()
ax= fig.add_subplot(3,3,1) # 将图纸分为三行三列，散点图为第一块位置
n = 128 # 128个点
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X) # 上色
# plt.axes([0.025,0.025,0.95,0.95])
ax.scatter(X,Y,s=75,c=T,alpha=0.5) # s：size，c：color
plt.xlim(-1.5,1.5),plt.xticks([])
plt.ylim(-1.5,1.5),plt.yticks([])
plt.axis()
plt.title("scatter")
plt.xlabel("x")
plt.ylabel("y")

# 绘制 柱状图
fig.add_subplot(332)
n = 10
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
plt.bar(X, +Y1, facecolor='#9999ff',edgecolor='white') # Y1 放在上面
plt.bar(X, -Y2, facecolor='#ff9999',edgecolor='white') # Y2 放在下面
for x,y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%0.2f' % y, ha='center', va='top')
for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.05, '%0.2f' % y, ha='center', va='bottom')

# 绘制 饼图
fig.add_subplot(333)
n = 20
Z = np.ones(n)
Z[-1] *= 2
plt.pie(Z, explode=Z * 0.05, colors=['%f' % (i / float(n)) for i in range(n)],
        labels=['%0.2f' % (i / float(n)) for i in range(n)])
plt.gca().set_aspect('equal')
plt.xticks([])
plt.yticks([])

# 绘制 折线图
fig.add_subplot(334)
n = 20
theta = np.arange(0, 2 * np.pi, 2 * np.pi /n)
radii = 10 * np.random.rand(n)
plt.plot(theta,radii)

# 绘制 极坐标图
fig.add_subplot(335, polar = True)
plt.polar(theta,radii)

# 绘制 热图
fig.add_subplot(336)
from matplotlib import cm
data = np.random.rand(3,3)
cmap = cm.Blues
map = plt.imshow(data, interpolation='nearest', cmap=cmap, aspect='auto', vmin=0, vmax=1)

# 绘制 3d 图
from mpl_toolkits.mplot3d import Axes3D
ax = fig.add_subplot(337, projection="3d")
ax.scatter(1,1,3,s=100)

# 绘制 热力图
fig.add_subplot(338)
def f(x,y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x **2 - y **2)
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

# plt.savefig("d:\\fig.png") # 保存最终绘制的图片到本地
plt.show() # 将画的所有图显示出来