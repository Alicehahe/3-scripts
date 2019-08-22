import xlrd
import os
import pymysql.cursors


path='/Users/qingjiao/Desktop/爱康全国地址.xls'
city_list=[]
branch_name=[]
legal_name=[]
address=[]
tel=[]

'创建数据库连接'
conn_db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='12345678',
    db='Ak_address',
    charset='utf8'
)
cursor = conn_db.cursor()
'打开表格'
xl = xlrd.open_workbook(path)
'获取第一张sheet'
sheet1=xl.sheet_by_index(0)
row_num = sheet1.nrows
col_num = sheet1.ncols


''''获取医院分布城市地点'
city_list= str(sheet1.col_values(1))

print('医院分布城市地点：',city_list)

'获取分院名称一列信息'
branch_name= str(sheet1.col_values(2,1))
print('分院名称：',branch_name)

'获取医院法定名称'
legal_name=str(sheet1.col_values(3,1))
print('医院法定名称：',legal_name)

'获取医院地址列表'
address=str(sheet1.col_values(4,1))
print('医院地址列表：',address)

'获取医院总机电话列表'
tel= str( sheet1.col_values(8,2))
print('总机电话列表：',tel)'''
ak_info=[]

for i in range(3,row_num):
    ak_info.append(sheet1.row_values(i,1,5)+sheet1.row_values(i,8,9))

print('infromation:',ak_info)

sql = 'insert into AK_Information(city_list,branch_name,legal_name,address,tel) values(%s,%s,%s,%s,%s)'
'''values=ak_info[0]
print(ak_info[0])
print(len(ak_info))
cursor.execute(sql,values)'''
for i in range(0,len(ak_info)):
    cursor.execute(sql,ak_info[i])

conn_db.commit()
cursor.close()

'''sql = 'insert into AK_Information(city_list,branch_name,legal_name,address,tel values(%s,%s,%s,%s)'
conn = db.cursor()
conn.execute(sql,tel)
conn.close()'''