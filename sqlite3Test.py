import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print(cursor.rowcount)
# cursor.execute('create table user (id varchar(20) primary key, name VARCHAR(20))')    # 创建一张表
cursor.execute('insert into user (id, name) values (\'1\', \'zhan\')')                # 插入一条学生数据
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()