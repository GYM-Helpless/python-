import pymysql
import re
import ssl
from urllib import request

dbhost='localhost'              #主机名
dbport=1111                     #端口号
dbuser='admin'                  #用户名
dbpwd='admin123'                #密码
datab='database_test_pysql'     #使用的数据库名
try:
    conn = pymysql.connect(host=dbhost,port=dbport,user=dbuser,password=dbpwd,database=datab)
    print('连接成功')
except pymysql.Error as e:
    print(pymysql.Error())

cur = conn.cursor()         #创建一个数据库对象
sql = 'insert into words (words,translation) values(%s,%s);'          #想要执行的sql语句

ssl._create_default_https_context = ssl._create_unverified_context    #全局取消证书验证

url = 'https://www.eol.cn/html/en/cetwords/cet4.shtml'                #爬取数据的网站
req = request.Request(url)          #创建一个request对象
res = request.urlopen(req)          #创建request的返回值

html = res.read().decode('utf-8')           #读取响应体，设置为utf-8格式
limt2 = '<p>(.*?\S)</p>'                    #正则表达式
a = re.findall(limt2,html)                  #使用正则表达式读取内容

del a[0:4]                                  #去除不需要的数据
for i in a:
    if i[0]==" ":
        #print("true")
        i=i[1: ]
        #print(i)
        if i[0]==" ":
            i = i[1: ]
            i.split(" ",1)
            cur.execute(sql,(i.split(" ",1)[0],i.split(" ",1)[1]))
        else:
            cur.execute(sql,(i.split(" ",1)[0],i.split(" ",1)[1]))
    else:
        cur.execute(sql,(i.split(" ",1)[0],i.split(" ",1)[1]))
conn.close()            #关闭数据库连接
