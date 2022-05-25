import pymysql

DBHOST='localhost'
username='root'
password='0718xjaqs'
dabase='test'
try:
    db=pymysql.connect(host=DBHOST,user=username,password=password,database=dabase)
    print("连接成功")
    cur=db.cursor() #声明一个游标
    sqlQuery='DROP TABLE IF EXISTS Student1'
    cur.execute(sqlQuery)
    print('数据表删除成功')
except pymysql.Error as e:
    print(str(e))
    db.rollback()