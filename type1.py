#!/usr/bin/python
# -*-coding:utf-8-*-

import urllib

class crawler:
'''
	only crawl one page, and not use regex to filter word 

'''

	# init variable 
	#self.path mean the path you want to crawller
	#self.htmlCode_Undecode mean the html code you got before you decode
	#self.htmlCode_Decode mean the html code you got after you decode

	def __init__(self,path):

		self.path = path
		self.htmlCode_Undecode = urllib.urlopen(path).read()
		self.htmlCode_Decode = self.htmlCode_Undecode.decode('utf8', 'ignore')
	
	#get all URL in onepage
	def getURL(self):

		(link_start,link_end) = (0,0)
		htmlCode = self.htmlCode_Decode

		while 1:
			shortName = self.htmlCode_Decode[link_start:]
			if 'href=\"' not in shortName and 'HREF=\"' not in shortName:
				break
			link_start,link_end = self.findUrl(link_start, link_end, htmlCode)

	#find Url in the htmlCode
	def findUrl(self, link_start, link_end, htmlCode):
		#let one line shorter than 80 column
		link_start = len('href=\"') + link_start
		link_start = htmlCode[link_start:].find('href=\"') + link_start

		link_end = htmlCode[link_start:].find('\"') + link_start
		if ".css" not in htmlCode[link_start:link_end]:
			print(self.filter_Url( htmlCode[link_start:link_end] ))
		return link_start,link_end

	#filter the URL do not have http or https
	def filter_Url(self,Path_get):
		if  "http" in  Path_get or "HTTP" in  Path_get :
			return Path_get
		elif "https" in Path_get or  "HTTPS" in Path_get:
			return Path_get
		else:
			Pos = Path_get.find('/')
			if Pos == 0:
				Path_get = Path_get[1:]
			return self.path + '/' + Path_get



#a = crawler('http://www.nchu.edu.tw/index1.php')
#print(a.path)
#print(a.htmlCode_Decode)
#print(a.htmlCode_Undecode)
#a.getURL()