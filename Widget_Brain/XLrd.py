import xlrd
import datetime

path = 'salesdata2019-1-3.xlsx'

inputWorkbook = xlrd.open_workbook(path)
sheet = inputWorkbook.sheet_by_index(0)
inputworksheet1 = inputWorkbook.sheet_by_index(1)
inputworksheet2 = inputWorkbook.sheet_by_index(2)

Sales = (sheet + inputworksheet1 + inputworksheet2)

print(Sales)

print(sheet.column(0, 0))



#print(inputworksheet1.nrows)
#print(inputworksheet1.ncols)
#print(inputworksheet1.cell_value(1, 0))

#print(inputworksheet2.nrows)
#print(inputworksheet2.ncols)
#print(inputworksheet2.cell_value(1, 0))



