import time
import sqlite3
cx = sqlite3.connect("d:/test.db") 
cur = cx.cursor()
#cur.execute("create table if not exists invest(id integer(4) primary key autoincrement, name varchar(128),code varchar(129), content varchar(255),percent integer)")
#f = open(time.strftime('%Y-%m-%d',time.localtime(time.time())) + '.txt','r')
data = ['1','2','3','4','5']
data1 = [1,2,3,4,5]
for i in data1:
    cur.execute("create table if not exists "&i&" (id integer(4) primary key autoincrement, name varchar(128),code varchar(129), content varchar(255),percent integer)")
print cur.execute("select name from sqlite_master").fetchall()[3][0]
#sqlite3 sql "select * INTO OUTFILE 'xxx.txt' from sqlite_master"

'''for line in f:
    #print line.decode("utf-8")
    #line.decode('gbk', 'ignore')
    data[1],data[2],data[3],data[4]= line.split(' ',3)
    #print data[0].decode("utf-8"),data[1],data[2].decode("utf-8"),data[3]
    #cur.execute("insert into invest(name,code,content,percent) values('%s',%s,'%s','%s')" %(data[0],data[1],data[2],data[3]))
    #cur.commit()
    data[1]=data[1].decode("utf-8")
    data[2]=data[2].decode("utf-8")
    data[3]=data[3].decode("utf-8")
    cur.execute("insert into invest values (?,?,?,?,?)",data)
    for i in data:
        print i

    #for i in data:
    #    cx.execute("insert into invest values (?,?,?,?,?)",i)
cx.commit()
cur.close()
cx.close()
'''


