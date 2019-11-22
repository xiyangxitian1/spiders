import xlrd

data = xlrd.open_workbook('a.xls')

sheet_names = data.sheet_names()
print(sheet_names)

table = data.sheet_by_index(0)

print(str(table.nrows))
print(str(table.ncols))

print(str(table.row_values(0)))
print(str(table.col_values(0)))

cel = table.cell(0, 1).value
print(cel)
