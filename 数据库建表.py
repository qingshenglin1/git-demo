import pymysql

DBHOST='localhost'
username='root'
password='0718xjaqs'
dabase='test'
try:
    db=pymysql.connect(host=DBHOST,user=username,password=password,database=dabase)
    print("连接成功")
    cur=db.cursor() #声明一个游标
    cur.execute('DROP TABLE IF EXISTS Student1')
    sqlQuery = "CREATE TABLE Student1(Name CHAR(20) NOT NULL ,Email CHAR(20),Age int )"
    cur.execute(sqlQuery)
    print("创建成功")
except pymysql.Error as e:
    print(str(e))
