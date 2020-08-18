import pymysql

#连接数据库 创建spider数据库
db = pymysql.connect(host='localhost',user='root', password='ybr080414', port=3306)
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version:', data)
cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
db.close()