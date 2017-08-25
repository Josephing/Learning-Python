a1=input("输入小时:")
b1=input("输入 分钟:")
c1=input("输入 秒:")
a1=int(a1)
b1=int(b1)
c1=int(c1)

c2=c1+30

if c2<=60:	
	b2=b1+5
else: 
	b2=b1+6
	c2=c2-60

if b2<=60:
	a2=a1
else:
	a2=a1+1
	b2=b2-60

if a2<24:
	a2=a2
else:
	a2=a2-24

print("5分30秒后的时间是:%d时%d分%d秒"%(a2,b2,c2))
