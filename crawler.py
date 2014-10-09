#!/usr/bin/python
# -*-coding:utf-8-*-

import urllib

from crawl import crawl 
from frontier import frontier


class crawler(crawl,frontier):
	def __init__(self, seed):
		frontier.__init__(self, seed )
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