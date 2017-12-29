import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,256,endpoint=True) # 定义横轴：[-π,π] 间有256个点，包括最后一个点
c = np.cos(x) # 定义余弦函数
s = np.sin(x) # 定义正弦函数
plt.figure(1) # 指定其为第一个图，标题栏会显示 Figure 1

plt.plot(x,c) # 画余弦函数，x 为自变量，c 为因变量
plt.plot(x,c,color="blue",linewidth=1.0,linestyle="-",label="Cos",alpha=0.5) # 画余弦函数，并为其指定线型：颜色为蓝色，线宽为1.0，线样式为直线，标签为COS，透明度为0.5

plt.plot(x,s) # 画正弦函数
plt.plot(x,s,"r.",label="Sin") # 画正弦函数，并为其指定线型：线样式为.，标签为Sin

ax = plt.gca() # 轴的编辑器
ax.spines["right"].set_color("none") # 将右轴颜色设为无，即隐藏右轴
ax.spines["top"].set_color("none") # 将上轴颜色设为无，即隐藏上轴
ax.spines["left"].set_position(("data",0)) # 将左轴位置移到数据为0的地方，即移到中间
ax.spines["bottom"].set_position(("data",0)) # 将底轴位置移到数据为0的地方，即移到中间
ax.xaxis.set_ticks_position("bottom") # 将 x 轴的刻度写在 x 轴的底部
ax.yaxis.set_ticks_position("left") # 将 y 轴的刻度写在 y 轴的左边

plt.xticks([-np.pi, -np.pi/2 ,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$']) # 第一个数组指定 x 轴每个刻度值的位置，第二个数组为标识的内容
plt.yticks(np.linspace(-1,1,5,endpoint=True)) # 给 y 轴标数字，[-1，1] 间标5个点，且最后一个点标出来
for label in ax.get_xticklabels() + ax.get_yticklabels(): # 得到 x 轴 和 y 轴的标签
    label.set_fontsize(16) # 设置标签的字体大小
    label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2)) # 设置标签的边框：背景颜色为白色，边缘颜色为透明，透明度为0.2

plt.legend(loc="upper left") # 图例偏上偏左（标签在图例里面）
plt.grid() # 显示出网格线
# plt.axis([-1,1,-0.5,1]) # 指定图的显示范围，[-1，1] 为 x 轴显示范围，[-0.5，1] 为 y 轴显示范围

plt.fill_between(x,np.abs(x)<0.5,c,c<0.5,color="green",alpha=0.25) # 在|x|<0.5，c<0.5 的区域涂色，填充颜色为绿色，透明度为0.25

# 在 x=1，y为[0.cos1]的区域做一条辅助线，线属性为：颜色为黄，线样式为虚线
t = 1
plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3,linestyle="--")
# 给刚刚画的辅助线做个注释：注释内容为cos(1)，注释文字的位置为cos1，注释文字的位置偏移(+10，+30)以免覆盖图形，offset points 用以指定(+10，+30)为相对位。箭头样式为 ->，箭头弧度为0.2
plt.annotate("cos(1)",xy=(t,np.cos(1)),xycoords="data",xytext=(+10,+30),textcoords="offset points",
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=0.2"))

plt.title("COS and SIN") # 给画出来的图加标题
plt.show()    # 将图显示出来