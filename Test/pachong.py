'''#-*_coding:utf-8_*_

import urllib
import urllib.request
url="http://www.baidu.com"
user_agent='Mozilla/4.0 (compatible;MSIE5.5;Windows NT)'
header={'User-Agent':user_agent}

data=urllib.request.urlopen(url).read()
data=data.decode('UTF-8')
print(data)
'''


import match
import os
import datetime
import json


	
	
def writeToTxt(list_name,file_path):
    try:
        #这里直接write item 即可，不要自己给序列化在写入，会导致json格式不正确的问题
        fp = open(file_path,"w+",encoding='utf-8')
        l = len(list_name)
        i = 0
        fp.write('[')
        for item in list_name:
            fp.write(item)
            if i<l-1:
                fp.write(',\n')
            i += 1
        fp.write(']')
        fp.close()
    except IOError:
        print("fail to open file")

#def getStr(item):
#   return json.dumps(item).replace('\'','\"')+',\n'



def createFile():
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    path = '/'+date
    if os.path.exists(path):
        return path
    else:
        os.mkdir(path)
        return path
def saveBlogs():
    for i in range(1,2):
        print('request for '+str(i)+'...')
        blogs = match.blogParser(i,5)
        #保存到文件
        path = createFile()
        writeToTxt(blogs,path+'/blog_'+ str(i) +'.json')
        print('第'+ str(i) +'页已经完成')
    return 'success'

result = saveBlogs()
print(result)