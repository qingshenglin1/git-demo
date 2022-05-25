import pymysql

DBHOST='localhost'
username='root'
password='0718xjaqs'
dabase='test'
try:
    db=pymysql.connect(host=DBHOST,user=username,password=password,database=dabase)
    print("连接成功")
    cur=db.cursor() #声明一个游标
    sqlQuery = "SELECT * FROM Student1"
    cur.execute(sqlQuery)
    results=cur.fetchall()
    for row in results:
        name=row[0]
        email=row[1]
        age=row[2]
        print(name,email,age)
except pymysql.Error as e:
    print(str(e))
db.close()