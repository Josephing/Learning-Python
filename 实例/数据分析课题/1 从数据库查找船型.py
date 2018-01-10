import xlrd
import xlwt

Workbook = xlrd.open_workbook('0 从数据库查找船型.xlsx')
wbk = xlwt.Workbook()
c = wbk.add_sheet('c',cell_overwrite_ok=True)

table1 = Workbook.sheets()[0]
table3 = Workbook.sheets()[3]

nrows1 = table1.nrows
nrows2 = table3.nrows

x1 = []
x2 = []
x22 = []

for i in range(nrows1):
	if i == 0:
		continue
	x1.append(table1.row_values(i)[:1])

for i in range(nrows2):
    if i == 0:
        continue
    x2.append(table3.row_values(i)[:1])

for i in range(nrows2):
    if i == 0:
        continue
    x22.append(table3.row_values(i)[1:2])

for m1,i1 in enumerate(x1):
    for m2,i2 in enumerate(x2):
        if i1==i2:
            c.write(m1+1, 3, "".join(x22[m2]))

wbk.save('abc.xls')