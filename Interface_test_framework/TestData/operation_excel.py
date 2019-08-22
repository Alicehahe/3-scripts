#coding:utf-8
'''
function:读取excel表中的测试用例
write on：2019-04-09 by hanlu
modules：xlrd模块用于读取excel
主要流程：
1.打开文件，获取具柄fp = open(file_path)
2.通过表格下标获取tables对象 tables=fp.sheets()[index]
3.可以获取总行数 tables.nrows
4.总列数 tables.ncols
5.也可以获取某一个单元格的内容 tables.cell_value(row,col)
'''
import requests
import xlrd

'''
操作excel原理代码
#打开文件，获取文件book对象
data = xlrd.open_workbook('/Users/qingjiao/Desktop/interface_testcase.xlsx')


#通过表格sheet下标得到table数据
tables = data.sheets()[0]

#获取总行数
print(tables.nrows)
#获取总列数
print(tables.ncols)

#获取某个单元格内的值，行和列都是从0开始
print(tables.cell_value(1,3))'''

#封装成类的高级用法
class Operation_Excel:
    #构造函数，初始化时候就拿到数据
    def __init__(self, file_path=None, sheet_id=None):
        #设置默认值None，不传使用默认值，传参使用对应的传入参数
        if file_path:
            self.file_path = file_path
            self.sheet_id = sheet_id
        else:
            self.file_path = '/Users/qingjiao/Desktop/interface_testcase.xlsx'
            self.sheet_id = 0
        self.tables = self.get_data()

    #获取sheet的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_path)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格个行数 tables.rows
    def get_lines(self):
        return self.tables.nrows

    #获取某一个单元格内容 cell_value(row,col)
    def get_cell_value(self,row,col):
        return self.tables.cell_value(row,col)

if __name__ == '__main__':
    opers = Operation_Excel()
    print(opers.get_lines())
    print(opers.get_cell_value(1,4))