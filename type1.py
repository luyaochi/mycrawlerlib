#!/usr/bin/python
# -*-coding:utf-8-*-

import urllib

class crawl:
#'''	only crawl one page, and not use regex to filter word '''

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
			link_start,link_end = self.seedsFinder(link_start, link_end, htmlCode)

	#find seeds in the htmlCode,seed mean url
	def seedsFinder(self, link_start, link_end, htmlCode):
		#let one line shorter than 80 column
		link_start,link_end = self.calulateLinkPosition(link_start, link_end, htmlCode)
		if ".css" not in htmlCode[link_start:link_end]:
			print(self.filter_Url( htmlCode[link_start:link_end]))
		return link_start,link_end

	#filter the URL do not have http or https
	def filter_Url(self,Path_get):
		if  ("http" in  Path_get) or ("HTTP" in  Path_get) :
			return Path_get
		elif "https" in Path_get or  "HTTPS" in Path_get:
			return Path_get
		else:
			Pos = Path_get.find('/')
			if Pos == 0:
				Path_get = Path_get[1:]
			return self.path + '/' + Path_get

	def show_current_URL(self):
		return self.path

	def calulateLinkPosition(self, link_start, link_end, htmlCode):
		link_start = htmlCode[link_start:].find('href=\"') + link_start
		link_start = len('href=\"') + link_start
		link_end = htmlCode[link_start:].find('\"') + link_start
		return link_start,link_end

class frontier:
	def __init__(self,seed = None):
		self.list_frontier = []
		self.init_frontier(seed)
 
	def init_frontier(self,seed):
		if seed == None:
			self.load_frontierFromDb()
		else:
			self.add_frontier(seed)
		return self.list_frontier

	def show_frontier(self):
		return self.list_frontier

	def add_frontier(self,seed):
		if seed not in self.list_frontier:
			self.list_frontier.append(seed)

	def del_frontier(self):
		return self.list_frontier.pop(0)

	def show_first_frontier(self):
		return self.list_frontier[0]

	def len_frontier(self):
		return len(self.list_frontier)


#not write
	def save_frontierToDb(self):
		pass
	
	def load_frontierFromDb(self):
		pass

class source:
	def saveData():
		pass

	def loadData():
		pass

class strategy:
	def bfgs():
		pass
	def dfs():
		pass

class crawler(crawl,frontier):
	def __init__(self, seed):
		frontier.__init__(self, seed)
		crawl.__init__(self, self.show_first_frontier())

	def seedsFinder(self,link_start, link_end, htmlCode):
		link_start,link_end = self.calulateLinkPosition(link_start, link_end, htmlCode)
		if ".css" not in htmlCode[link_start:link_end]:
			filterURL = self.filter_Url( htmlCode[link_start:link_end])
			self.add_frontier(filterURL)
		return link_start,link_end

	def getURL(self):
		crawl.getURL(self)
		self.del_frontier()