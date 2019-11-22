import xlwt

xls = xlwt.Workbook()
sheet1 = xls.add_sheet('Sheet1')

Font0 = xlwt.Font()
Font0.name = 'Times New Roman'
Font0.colour_index = 2
Font0.bold = True  # 加粗
style0 = xlwt.XFStyle()
style0.font = Font0
# 添加字段
sheet1.write(0, 0, '字段1', style0)
sheet1.write(0, 1, '字段2')

xls.save('a.xls')
