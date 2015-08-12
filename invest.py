#!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
import re
import urllib2
import urllib
from time import sleep
#from bs4 import BeautifulSoup
#hosturl = 'http://xueqiu.com/P/ZH084118'
hosturl = ['http://xueqiu.com/cubes/discover/rank/cube/list.json?category=10&count=10&market=cn&page=1']
#f = open(time.strftime('%Y-%m-%d',time.localtime(time.time())) + '.txt', 'w+');
def worm(url):
    #print url
    HEADER = {

        'User-Agent': 'Mozilla/5.0 (Wsindows NT 6.1; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Host':"xueqiu.com",
        'Cookie':'s=j2q124tpdg; __utma=1.542938384.1433140791.1433383582.1433992321.6; __utmz=1.1433992321.6.5.utmcsr=offlintab.firefoxchina.cn|utmccn=(referral)|utmcmd=referral|utmcct=/; Hm_lvt_1db88642e346389874251b5a1eded6e3=1433298229,1433301115,1433383582,1433992322; bid=451fd9a0c4aaac8a62796193edfe06b6_iadjg0bk; xq_a_token=4f580892581d654158166fb855d4bd95d9b7ce54; xq_r_token=d6394567c6ac3caf4bb387337290b0a9d1c4533d; xqat=4f580892581d654158166fb855d4bd95d9b7ce54; xq_token_expire=Mon%20Jun%2029%202015%2010%3A12%3A47%20GMT%2B0800%20(CST); xq_is_login=1; __utmb=1.21.9.1433992685576; __utmc=1; __utmt=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1433992641'
    }


    urlrequest = urllib2.Request(url,None,HEADER)
    urlresponse = urllib2.urlopen(urlrequest)
    html = urlresponse.read()
    html_u = html.decode('utf8')

    pattern_name = re.compile("<span class=\"name\">(.*?)<\/span>")
    pattern_symbol = re.compile("<span class=\"symbol\">(.*?)<\/span>")

    res_name = pattern_name.findall(html_u)
    res_symbol = pattern_symbol.findall(html_u)
    #print res_name[0],res_symbol[0]


    pattern1 = re.compile("cubePieData(.+),\"color")
    res1 = pattern1.search(html_u).group()
    pattern2 = re.compile(u"[\u4e00-\u9fa5]+")
    pattern3 = re.compile("weight\":\d+\.\d+|weight\":\d+")
    a = pattern2.findall(res1)
    b = pattern3.findall(res1)
    #c = pattern4.match(res1).group()
    #for i in b:
    #    i=i.replace("weight\":","")
    #    print i
    print len(a)
    print url
    
    
    
    for i in range(0,len(a)):
        b[i]= b[i].replace("weight\":","")
        f = open(res_name[0] + '.txt', 'a');
        f.write(res_name[0])
        f.write(" ")
        f.write(res_symbol[0])
        f.write(" ")
        f.write(a[i])
        f.write(" ")
        f.write(b[i])
        f.write(" ")
        f.write(time.strftime('%Y-%m-%d',time.localtime(time.time())))
        f.write('\n')
        f.close()
    
   
   
for i in hosturl:
    worm(i)
    sleep(5)
#worm(hosturl)