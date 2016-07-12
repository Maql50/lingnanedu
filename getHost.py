import urllib2
import re

def getpage(url):
	page = urllib2.urlopen(url).read()
	return page

def gettds(html_cont):
	alllines = re.findall('class="blob-code blob-code-inner js-file-line">(.*?)</td>', html_cont, re.S);
	return alllines

if __name__ == '__main__':
	url = "https://github.com/racaljk/hosts/blob/master/hosts"
	page = getpage(url)
	for line in gettds(page):
		print line