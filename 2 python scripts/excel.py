#coding:utf-8
#!/usr/bin/python

import xlrd

data = xlrd.open_workbook(r"C:\Python27:\Book1.xlsx")
table = data.sheets()

print table

table1 = data.sheets()[0]
rows = table.nrows
for i in range(rows):
    print table.row_values(i)
    
