# 导入模块
import xlrd
# 打开excel
data=xlrd.open_workbook('d:\data.xls')

# 1.打开并打印文件中有内容的Sheet的名称
sheet_names=data.sheet_names()
print("sheet names:",sheet_names)
# 通过索引顺序获取Sheet1的内容,0代表第一张Sheet
table=data.sheet_by_index(0)

# 2.获取第一张工作表的行数和列数
nrows=table.nrows
print("行数:",nrows)
ncols=table.ncols
print("列数:",ncols)

# 3.分别获取第一张工作表的第2行和第2列的值（数组）
print("第2行的值:",table.row_values(2))
print("第2列的值:",table.col_values(2))

# 4.分别获取特定单元格的值
print("第1行，第1列的值:",table.cell_value(0,0))
print("第1行，第2列的值:",table.cell_value(0,1))