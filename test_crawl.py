#!/usr/bin/python
# -*-coding:utf-8-*-

import unittest
import urllib
from crawl import crawl

path = 'http://www.nchu.edu.tw/index1.php'

#test crawl
class TestCrawl(unittest.TestCase):
	def setUp(self):
		self.crawl = crawl(path)

	#test initialize variable
	def test_path(self):
		Unit1 = path
		Unit2 = self.crawl.path
		self.assertEqual(Unit1,Unit2)

	def test_htmlCode_Undecode(self):
		Unit1 = urllib.urlopen(path).read()
		Unit2 = self.crawl.htmlCode_Undecode
		self.assertEqual(Unit1,Unit2)

	def test_htmlCode_decode(self):
		shortName = self.crawl
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
		Unit1 = self.crawl.seedsFinder(0,0,'')
		Unit2 = (5,4)
		self.assertEqual(Unit1,Unit2)

	#test filter url
	def test_filter_Url(self):
		Unit1 = self.crawl.filter_Url('123456')
		Unit2 = self.crawl.path + '/123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_with_slash(self):
		Unit1 = self.crawl.filter_Url('/123456')
		Unit2 = self.crawl.path + '/123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_HTTPS(self):
		Unit1 = self.crawl.filter_Url('HTTPS://123456')
		Unit2 = 'HTTPS://123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_https(self):
		Unit1 = self.crawl.filter_Url('https//123456')
		Unit2 = 'https//123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_HTTP(self):
		Unit1 = self.crawl.filter_Url('HTTP://123456')
		Unit2 = 'HTTP://123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_http(self):
		Unit1 = self.crawl.filter_Url('http://123456')
		Unit2 = 'http://123456'
		self.assertEqual(Unit1,Unit2)

	def test_show_current_URL(self):
		Unit1 = self.crawl.show_current_URL()
		Unit2 = self.crawl.path
		self.assertEqual(Unit1,Unit2)

	def test_calulateLinkPosition(self):
		htmlCode = '<a href=\"https://www.google.com\">'
		Unit1 = self.crawl.calulateLinkPosition(0, 0, htmlCode)
		Unit2 = (htmlCode.find('href=\"')+len('href=\"'),htmlCode.find('\">'))
		self.assertEqual(Unit1,Unit2)


if __name__ == '__main__':
	#unittest.main()

	suite = unittest.TestLoader().loadTestsFromTestCase(TestCrawl)
	unittest.TextTestRunner(verbosity=2).run(suite)
