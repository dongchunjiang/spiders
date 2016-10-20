#-*- coding: UTF-8 -*-
import urllib
import urllib2
import re
 
page = 2
url = 'http://www.qiushibaike.com/text/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?target.*?<img.*?<h2>(.*?)</h2>'+
        '.*?content">.*?<span>(.*?)</span>.*?</a>',re.S)
    items = re.findall(pattern,content)
    replacebr = re.compile('<br/>')
    for item in items:
        print item[0]
        print u"发表内容------>"
        print re.sub(replacebr,'\n',item[1])
        print "--------------------------------------------------"
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
