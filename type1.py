#!/usr/bin/python
# -*-coding:utf-8-*-

import urllib



class crawler:

	__init__(self,Path):
		self.Path = Path
		self.htmlCode_Undecode = urllib.urlopen(Path)
		self.htmlCode_Decode = htmlCode_Undecode.read().decode('utf8', 'ignore')
	
	#find Url in the htmlCode
	def findUrl(link_start,link_end,htmlCode):
		link_start = htmlCode_Decode[link_start:].find('href=\"') + len('href=\"') + link_start
		link_end = htmlCode_Decode[link_start:].find('\"') + link_start
		if ".css" not in htmlCode_Decode[link_start:link_end]:
			filter_Url(htmlCode_Decode[link_start:link_end])
		return link_start,link_end
	
	#filter the URL do not have http or https
	def filter_Url(Path_get):
		if  "http:/" in  Path_get or "HTTP:/" in  Path_get :
			print(Path_get)
		elif "https:/" in Path_get or  "HTTPS:/" in Path_get:
			print(Path_get)
		else:
			print(Path+ '/' +Path_get)

	#get all URL in onepage
	def getURL():
		while 1:
			if 'href=\"' not in htmlCode_Decode[link_start:] and 'HREF=\"' not in htmlCode_Decode[link_start:]:
			break

		link_start,link_end = findUrl(link_start, link_end, htmlCode_Decode)





