# encoding: utf-8
import urllib2
import re


def getpage(url):
	page = urllib2.urlopen(url).read()
	return unicode(page, "utf-8").encode("utf-8")

def getweather(page):
	return re.search('<div class="wd_cmh">深圳</div><div class="wd_cmc"><table class="wd_cm_table">(.*?)</table>', page , re.S).group(1)

if __name__ == '__main__':
	url = "http://weather.sina.com.cn/china/guangdongsheng/"
	page =  getpage(url)
	print getweather(page)
