# coding=utf-8
import mysql.connector

# mysql的sql占位符是 %s
try:
    # use_unicode=True表示mysql的DB-API始终返回unicode
    conn = mysql.connector.connect(host='localhost', user='root', password='zhhszhx', use_unicode=True)
    cursor = conn.cursor()
    # 判断数据库test是否存在
    cursor.execute('select * from information_schema.SCHEMATA where SCHEMA_NAME=%s', ('test',))
    dbs = cursor.fetchall()
    if not dbs:
        cursor.execute('create database if not exists test')
        # 选择数据库
        conn.database = 'test'
        cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
        cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
        print cursor.rowcount
        conn.commit()
        cursor.close()
        cursor = conn.cursor()
    else:
        conn.database = 'test'

    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    print values

except mysql.connector.Error as e:
    print e
finally:
    cursor.close()
    conn.close()

