#!/usr/bin/python
# -*-coding:utf-8-*-

import unittest
import urllib
from crawler import crawler

path = 'http://www.nchu.edu.tw/index1.php'

#test frontier
class TestCrawler(unittest.TestCase):
	#test initialize variable
	def setUp(self):
		self.crawler = crawler(path)

	def test_init_frontier(self):
		Unit1 = [path]
		Unit2 = self.crawler.init_frontier(path)
		self.assertEqual(Unit1,Unit2)

	#def test_list_frontier_none(self):
	#	#initialize
	#	self.crawler = crawler()
	#	Unit1 = []
	#	Unit2 = self.crawler.list_frontier
	#	self.assertEqual(Unit1,Unit2)

	def test_list_frontier_path(self):
		#initialize
		self.crawler = crawler(path)
		Unit1 = [path]
		Unit2 = self.crawler.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_show_frontier(self):
		Unit1 = self.crawler.show_frontier()
		Unit2 = self.crawler.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_add_frontier_notSamePath(self):
		self.crawler.add_frontier('secondPath')
		Unit1 = self.crawler.show_frontier()
		Unit2 = self.crawler.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_add_frontier_SamePath(self):
		self.crawler.add_frontier('Path')
		Unit1 = len(self.crawler.show_frontier())
		Unit2 = len(self.crawler.list_frontier)
		self.assertEqual(Unit1,Unit2)

	def test_del_frontier(self):
		self.crawler.add_frontier(path)
		self.crawler.add_frontier(path)
		Unit1 = len(self.crawler.show_frontier())
		self.crawler.del_frontier()
		Unit2 = len(self.crawler.show_frontier())
		self.assertEqual(Unit1,Unit2+1)

	def test_show_first_frontier(self):
		Unit1 = self.crawler.list_frontier[0]
		Unit2 = self.crawler.show_first_frontier()
		self.assertEqual(Unit1,Unit2)

	def test_len_frontier(self):
		Unit1 = len(self.crawler.show_frontier())
		Unit2 = self.crawler.len_frontier()
		self.assertEqual(Unit1,Unit2)


	#test initialize variable
	def test_path(self):
		Unit1 = path
		Unit2 = self.crawler.path
		self.assertEqual(Unit1,Unit2)

	def test_htmlCode_Undecode(self):
		Unit1 = urllib.urlopen(path).read()
		Unit2 = self.crawler.htmlCode_Undecode
		self.assertEqual(Unit1,Unit2)

	def test_htmlCode_decode(self):
		shortName = self.crawler
		Unit1 = shortName.htmlCode_Undecode.decode('utf8', 'ignore')
		Unit2 = shortName.htmlCode_Decode
		self.assertEqual(Unit1,Unit2)
	
	#not finish
	#test get URL
	#def test_getURL(self):
	#	Unit1 = self.crawl.getURL()
	#	Unit2 = self.crawl
	#	self.assertEqual(Unit1,Unit2)
	
	#test find findUrl
	def test_seedsFinder(self):
		Unit1 = self.crawler.seedsFinder(0,0,'')
		Unit2 = (5,4)
		self.assertEqual(Unit1,Unit2)

	#test filter url
	def test_filter_Url(self):
		Unit1 = self.crawler.filter_Url('123456')
		Unit2 = self.crawler.path + '/123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_with_slash(self):
		Unit1 = self.crawler.filter_Url('/123456')
		Unit2 = self.crawler.path + '/123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_HTTPS(self):
		Unit1 = self.crawler.filter_Url('HTTPS://123456')
		Unit2 = 'HTTPS://123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_https(self):
		Unit1 = self.crawler.filter_Url('https//123456')
		Unit2 = 'https//123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_HTTP(self):
		Unit1 = self.crawler.filter_Url('HTTP://123456')
		Unit2 = 'HTTP://123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_http(self):
		Unit1 = self.crawler.filter_Url('http://123456')
		Unit2 = 'http://123456'
		self.assertEqual(Unit1,Unit2)

	def test_show_current_URL(self):
		Unit1 = self.crawler.show_current_URL()
		Unit2 = self.crawler.path
		self.assertEqual(Unit1,Unit2)

	def test_calulateLinkPosition(self):
		htmlCode = '<a href=\"https://www.google.com\">'
		Unit1 = self.crawler.calulateLinkPosition(0, 0, htmlCode)
		Unit2 = (htmlCode.find('href=\"')+len('href=\"'),htmlCode.find('\">'))
		self.assertEqual(Unit1,Unit2)


if __name__ == '__main__':

	suite = unittest.TestLoader().loadTestsFromTestCase(TestCrawler)
	unittest.TextTestRunner(verbosity=2).run(suite)