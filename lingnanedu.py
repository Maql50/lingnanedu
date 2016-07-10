# encoding:utf-8
import requests
import sys
import urllib2
import urllib
import re
import cookielib

reload(sys)
sys.setdefaultencoding('utf-8')
#获取表格
def gettable(score_html):
	trs = re.search('<table class="datelist" cellspacing="0" cellpadding="3" border="0" id="Datagrid1" style="DISPLAY:block">(.*)</table>',score_html, re.S).group(1)
	print trs
	return trs;

#获取首页html
def getMainPage(url):
	html_cont = requests.get(url)
	html_cont.encoding = 'gb2312'
	return html_cont.text

#获取页面viewstatus
def getviewstatus(html_cont):
	return re.search('<input type="hidden" name="__VIEWSTATE" value="(.*?)" />', html_cont, re.S).group(1)

#获取名字
def getName(page, id):
	return  re.search('<span id="xhxm">'+id+'  (.*?)同学</span></em>', page, re.S).group(1)

#输出内容
def output(html_score):
	f = open("e://1//score.html","a")
	f.write("<html>")
	f.write("<head>")
	f.write('<meta http-equiv="content-type" content="text/html; charset=utf-8" />')
	f.write("</head>")
	f.write("<body>")
	f.write("<table border='1px'>")
	f.write(gettable(html_score))
	f.write("</table>")
	f.write("</body>")
	f.write("</html>")


if __name__ == '__main__':	
	#初始化基本内容
	url = 'http://202.192.143.243/(51gpbo45h4ah5yrvylalsu45)/default6.aspx'
	id = '2013874116'
	psw = 'zc12230109'

	page = getMainPage(url)

	#设置post数据
	postdate = urllib.urlencode({
		'__VIEWSTATE':getviewstatus(page),
		'tnameXw':'yhdl',
		'tbtnsXw':'yhdl|xwxsdl',
		'txtYhm':id,
		'txtXm':psw,
		'txtMm':psw,
		'rblJs':'(unable to decode value)',
		'btnDl':'(unable to decode value)'
	})

	#设置http头
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}

	#设置cookie
	cookie = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPHandler(cookie))
	myrequest = urllib2.Request(url, postdate, headers)
	loginPage = opener.open(myrequest).read()
	page = unicode(loginPage, 'gb2312').encode("utf-8") 

	getdata = urllib.urlencode({
		'xh':id,
		'xm':unicode(getName(page, id),'utf-8').encode('gb2312'),
		'gnmkdm':'N121605'
	})
 


	head = {
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding':'gzip, deflate, sdch',
		'Accept-Language':'zh-CN,zh;q=0.8',
		'Cache-Control':'no-cache',
		'Connection':'keep-alive',
		'Content-Type':'application/x-www-form-urlencoded',
		'Host':'202.192.143.243',
		'Cookie':cookie,
		'Origin':'http://222.24.19.201',
		'Pragma':'no-cache',
		'Upgrade-Insecure-Requests':1,		
		'Referer':'http://202.192.143.243/(51gpbo45h4ah5yrvylalsu45)/xs_main.aspx?xh='+getdata,
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
		}

 	myrequest = urllib2.Request('http://202.192.143.243/(51gpbo45h4ah5yrvylalsu45)/xscjcx.aspx?'+getdata, None, head)
	#获取第二个登录页面
	loginPage = unicode(opener.open(myrequest).read(), 'gb2312').encode('utf-8')
 

	data = urllib.urlencode({
		"__EVENTTARGET": "",
		"__EVENTARGUMENT":"",
		"__VIEWSTATE":getviewstatus(loginPage),
		"btn_zcj":unicode("历年成绩",'utf-8').encode('gb2312'),
		"hidLanguage":"",
		"ddlXN":"",
		"ddlXQ":"",
		"ddl_kcxz":""
	}) 

	myrequest = urllib2.Request('http://202.192.143.243/(51gpbo45h4ah5yrvylalsu45)/xscjcx.aspx?'+getdata,data, head)
	#获取第三个页面，即成绩页面
	html = opener.open(myrequest)
	result = unicode(html.read(), 'gb2312').encode('utf-8')
	output(result)
 


