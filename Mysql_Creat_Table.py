#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author :Alvin.xie
# @Time :2017-11-22 14:37
# @file :maketable.py

import MySQLdb

def connect_mysql():
    db_config = {
        'host': '10.89.1.10',
        'port': 3306,
        'user': 'demo',
        'passwd': '123qaz',
        'db': 'python_test',
        'charset': 'utf8'
    }
    cnx = MySQLdb.connect(**db_config)
    return cnx


if __name__ == '__main__':
    cnx = connect_mysql()
    cus = cnx.cursor()


student = '''create table Student(
        StdID int not null,
        StdName varchar(100) not null,
        Gender enum('M', 'F'),
        Age tinyint
)'''


course = '''create table Course(
        CouID int not null,
        CName varchar(50) not null,
        TID int not null
)'''


score = '''create table Score(
            SID int not null,
            StdID int not null,
            CID int not null,
            Grade int not null
)'''


teacher = '''create table Teacher(
                TID int not null,
                TName varchar(100) not null
)'''


tmp = '''set @i := 0;
        create table tmp as select (@i := @i + 1) as id from information_schema.tables limit 10;
    '''
try:
    cus.execute(student)
    cus.execute(course)
    cus.execute(score)
    cus.execute(teacher)
    cus.execute(tmp)
    cus.close()
    cnx.commit()
except Exception as e:
    cnx.rollback()
    print('error')
    raise e
finally:
    cnx.close()