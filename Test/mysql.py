#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Jankcy"

#from selenium import webdriver      
#from selenium.webdriver.common.keys import Keys      
#import selenium.webdriver.support.ui as ui           
import re  
import time  
import os  
import codecs  
import pymysql  

#def mysql():
start_t=time.time()
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='yangfan', db='cms', charset='utf8')  
#cur=conn.cursor() #数据库游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)  
        #报错:UnicodeEncodeError: 'latin-1' codec can't encode character  
		#conn.set_character_set('utf8')  
		#cur.execute('SET NAMES utf8;')  
		#cur.execute('SET CHARACTER SET utf8;')  
		#cur.execute('SET character_set_connection=utf8;')	
#sql = "select * from cms_comment";
#增加数据
sql = "INSERT INTO cms_comment (user,cid,content,date,manner,sustain,oppose) VALUES ( '%s','%d','%s',str_to_date('%s','%%m-%%d-%%Y %%h:%%i:%%s'),'%d','%d','%d')"
data = ('雷军', 23, '插入下一个评论!','5-30-2017 12:23:30',0,1,0)	
conn.commit()	
result = cur.execute(sql%data)
		# 获取剩余结果的第一行数据
print('成功插入', cur.rowcount, '条数据')
print(result)
# 修改数据
sql = "UPDATE cms_comment SET user = '%s' WHERE user = '%s' "
data = ('leijun', '雷军')
cur.execute(sql%data)
print('成功修改', cur.rowcount, '条数据')
# 查询数据
sql = "SELECT id,user,cid,date FROM cms_comment WHERE user = '%s' "
data = ('leijun')
cur.execute(sql % data)
for row in cur.fetchall():
    print("id:%s\tName:%s\t date:%s" %(row['id'],row['user'],row['date']))
print('共查找出', cur.rowcount, '条数据')


#删除数据
sql = "DELETE FROM cms_comment WHERE user = '%s' LIMIT %d"
data = ('lei', 1)
cur.execute(sql % data)
print('成功删除', cur.rowcount, '条数据')
# 事务处理
sql_1 = "UPDATE cms_comment SET cid = cid + 100 WHERE id = 52 "
sql_2 = "UPDATE cms_comment SET cid = cid + 110 WHERE id = 55 "
try:
    cur.execute(sql_1)  
    cur.execute(sql_2)
except Exception as e:
    conn.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    conn.commit()  # 事务提交
    print('事务处理成功', cur.rowcount)
#事务处理END
#row_1 = cur.fetchone()
#print(row_1)
		# 获取剩余结果前n行数据
#row_2 = cur.fetchmany(3)
#print(row_2)
row_3 = cur.fetchall()
station=[]
#print(row_3)
		# 获取剩余结果所有数据
		# row_3 = cursor.fetchall()
i=0
for items in row_3:
	i+=1

#	station[i]=items
#	print(str(items['date']))
	
#print(station)
	#print("id:"+str(items[0])+"name:"+str(items[1]))
	#print(items)
end_t=time.time()
spend_t=end_t-start_t
print("%3.2fs,%ds,%ds,"%(spend_t,start_t,end_t))
conn.commit()
cur.close()  
conn.close()  
#mysql()		