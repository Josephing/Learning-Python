# 光滑曲线
import xlrd
import xlwt
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

Workbook = xlrd.open_workbook('上行.xlsx')
wbk = xlwt.Workbook()
c = wbk.add_sheet('c',cell_overwrite_ok=True)
table1 = Workbook.sheets()[0]
nrows1 = table1.nrows

x4 = []
x9 = []
for i in range(nrows1):
	if i == 0:
		continue
	x4.append(table1.row_values(i)[4:5])
print(x4)
for i in range(nrows1):
    if i == 0:
        continue
    x9.append(table1.row_values(i)[9:10])
print(x9)

dd = []
for t in range(0,50,10):
    cc = []
    for L in range(10,110,10):
        js = 0
        for m4,i4 in enumerate(x4):
            if (float(x4[m4][0])>L and float(x4[m4][0])<=L+10) and (float(x9[m4][0])>t and float(x9[m4][0])<=t+10):
                js = js + 1
        cc.append(js)
    #print(cc)
    dd.append(cc)
dd = np.array(dd)
print(dd)

zxsum = np.sum(dd,axis=0)
hxsum = np.sum(dd,axis=1)
print(zxsum)

gl = dd/zxsum/10
print(sum(sum(gl)))

x = list(range(10,110,10))
y0 = gl[0]*100
y1 = gl[1]*100
y2 = gl[2]*100
y3 = gl[3]*100
y4 = gl[4]*100

x = np.array(x)
xnew = np.linspace(x.min(), x.max(), 300)
power_smooth0 = spline(x, y0, xnew)
power_smooth1 = spline(x, y1, xnew)
power_smooth2 = spline(x, y2, xnew)
power_smooth3 = spline(x, y3, xnew)
power_smooth4 = spline(x, y4, xnew)


def 去负数(power_smooth, num):
    global smooth
    smooth =[]
    for i in power_smooth:
        if i >= 0:
            smooth.append(i)
        else:
            i = 0
            smooth.append(i)
去负数(power_smooth0,0)
smooth0 = smooth
去负数(power_smooth1,1)
smooth1 = smooth
去负数(power_smooth2,2)
smooth2 = smooth
去负数(power_smooth3,3)
smooth3 = smooth
去负数(power_smooth4,4)
smooth4 = smooth

plt.plot(x,y0,"*")
plt.plot(x,y1,"*")
plt.plot(x,y2,"*")
plt.plot(x,y3,"*")
plt.plot(x,y4,"*")
plt.plot(xnew, smooth0, label="(0,10]min", linestyle = '--')
plt.plot(xnew, smooth1,label="(10,20]min", linestyle = '--')
plt.plot(xnew, smooth2,label="(20,30]min", linestyle = '--')
plt.plot(xnew, smooth3,label="(30,40]min",linestyle = '--')
plt.plot(xnew, smooth4,label="大于40min",linestyle = '--')

plt.xlabel("船长 L(m) "+"（注：50代表船长在(50,60]间)")
plt.ylabel('概率密度 %')
plt.title('船长与进厢时间关系图(上行)')

new_ticks = range(10,110,10)
plt.xticks(new_ticks)
plt.legend(loc='upper right',ncol=3)

plt.show()