# coding=utf-8
import sqlite3, os

# os.path.exists既可以判断文件夹路径，又可以判断文件路径，是否存在
if not os.path.exists('test.db'):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
    cursor.execute('INSERT INTO user (id, name) VALUES (\'1\',\'Michael\')')
    # rowcount返回影响的行数
    print cursor.rowcount
    cursor.close()
    conn.commit()
    conn.close()

# 在try中定义的变量在except和finally中也可以访问，这点跟C#不一样
try:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    # ?表示占位符，sql语句带有参数时使用，有几个参数就有几个?占位符，按先后顺序一一对应
    cur.execute('select * from user where id=?', ('1',))
    # fetchall()返回的是一个list，list里的每个元素都是一个tuple，对应一行记录
    values = cur.fetchall()
    print values
except sqlite3.Error as e:
    print e
finally:
    cur.close()
    conn.close()

