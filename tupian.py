import pymysql

db = pymysql.connect(host='localhost',port=3306,user='root',passwd='123456',
                     database='tupian',charset='utf8')


#获取游标
cur = db.cursor()

# with open('汤唯.jpg','rb') as f:
#     data = f.read()
#
# sql ="insert into ph values (1,%s,%s)"
# cur.execute(sql,[data,'初恋'])
# db.commit()

# 提取图片
sql = "select mean from ph \
where ex='初恋'"
cur.execute(sql)
data = cur.fetchone()[0]
with open('1.jpg','wb') as f:
    f.write(data)


db.close()

