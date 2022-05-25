import pymysql

DBHOST='localhost'
username='root'
password='0718xjaqs'
dabase='test'
try:
    db=pymysql.connect(host=DBHOST,user=username,password=password,database=dabase)
    print("连接成功")
    cur=db.cursor() #声明一个游标
    sqlQuery1 = " INSERT INTO Student1 (Name, Email, Age) VALUE (%s,%s,%s) "
    value = ('tom', '123456@163.com', 10)
    cur.execute(sqlQuery1, value)
    db.commit()
    print('数据插入成功！')
    db.close()
except pymysql.Error as e:
    print(str(e))