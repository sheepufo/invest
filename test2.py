import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')
a = 'aa ZH028305 aa 14.17'
b = a.split(' ',3)
print b 
print os.path.split(os.path.realpath(__file__))[0]