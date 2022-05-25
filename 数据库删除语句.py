import pymysql

DBHOST='localhost'
username='root'
password='0718xjaqs'
dabase='test'
try:
    db=pymysql.connect(host=DBHOST,user=username,password=password,database=dabase)
    print("连接成功")
    cur=db.cursor() #声明一个游标
    sqlQuery = "DELETE FROM Student1 where Name=%s"
    value = ('Join')
    cur.execute(sqlQuery,value)
    db.commit()
    print('数据删除成功')
except pymysql.Error as e:
    print(str(e))
    db.rollback()