import xlrd
import os
import pymysql.cursors


path='/Users/qingjiao/Desktop/爱康全国地址.xls'
city_list=[]
branch_name=[]
legal_name=[]
address=[]
tel=[]
city = ['北京','上海','广州','深圳','南京','成都','杭州','福州','天津','苏州',
        '重庆','长春','常州','江阴','沈阳','银川','潍坊','烟台','威海','武汉','长沙','佛山','宁波','西安','芜湖']

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
#获取总行数
row_num = sheet1.nrows
#获取总列数
col_num = sheet1.ncols

ak_info=[]

for i in range(2,row_num):
    ak_info.append(sheet1.row_values(i,1,5)+sheet1.row_values(i,8,9))

print('infromation:',ak_info)

sql = 'insert into AK_Information(city_list,branch_name,legal_name,address,tel) values(%s,%s,%s,%s,%s)'

for i in range(0,len(ak_info)):
    #print(ak_info[i][0])
    for j in city:
        if j in ak_info[i][2] or j in ak_info[i][1] or ak_info[i][3] and ak_info[i][0] == '':
            ak_info[i][0] = j
    if '爱康国宾 ' in ak_info[i][1]:
       ak_info[i][1]=ak_info[i][1][5:]
       print(ak_info[i][1])
    if '爱康国宾' in ak_info[i][1]:
       ak_info[i][1] = ak_info[i][1][4:]

    #将数据插入数据库中
    cursor.execute(sql,ak_info[i])

conn_db.commit()
cursor.close()