# -*- coding: utf-8 -*-
import re
import time

#pattern = re.compile("\"name\":(.+),\"color")

res = '<span class="name">JesseBond</span>'
res1 = '啊你好aaaa啊'
res2 = res.decode('utf8')
print len(res2)
pattern2 = re.compile("weight\":\d+\.\d+|weight\":\d+")
pattern1 = re.compile("a")
pattern3 = re.compile("span class=\"name\"")
b = pattern3.findall(res)
print b
#a = pattern2.findall(res2)
#for i in a :
#    i=i.replace("weight\":","")
#    print i

print type(time.strftime('%Y-%m-%d',time.localtime(time.time())))

#print 'Html is encoding by : %',chardet.detect(GetHtml('http://xueqiu.com/P/ZH068465'))