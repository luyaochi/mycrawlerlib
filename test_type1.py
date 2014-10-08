#!/usr/bin/python
# -*-coding:utf-8-*-

import unittest
import urllib

from type1 import crawle

path = 'http://www.nchu.edu.tw/index1.php'

#test crawle
class TestCrawle(unittest.TestCase):
	def setUp(self):
		self.crawle = crawle(path)

	#test initialize variable
	def test_path(self):
		Unit1 = path
		Unit2 = self.crawle.path
		self.assertEqual(Unit1,Unit2)

	def test_htmlCode_Undecode(self):
		Unit1 = urllib.urlopen(path).read()
		Unit2 = self.crawle.htmlCode_Undecode
		self.assertEqual(Unit1,Unit2)

	def test_htmlCode_decode(self):
		shortName = self.crawle
		Unit1 = shortName.htmlCode_Undecode.decode('utf8', 'ignore')
		Unit2 = shortName.htmlCode_Decode
		self.assertEqual(Unit1,Unit2)
	
	#not finish
	#test get URL
	#def test_getURL(self):
	#	Unit1 = self.crawle.getURL()
	#	Unit2 = self.crawle
	#	self.assertEqual(Unit1,Unit2)
	
	#test find findUrl
	def test_seedsFinder(self):
		Unit1 = self.crawle.seedsFinder(0,0,'')
		Unit2 = (5,4)
		self.assertEqual(Unit1,Unit2)

	#test filter url
	def test_filter_Url(self):
		Unit1 = self.crawle.filter_Url('123456')
		Unit2 = self.crawle.path + '/123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_with_slash(self):
		Unit1 = self.crawle.filter_Url('/123456')
		Unit2 = self.crawle.path + '/123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_HTTPS(self):
		Unit1 = self.crawle.filter_Url('HTTPS://123456')
		Unit2 = 'HTTPS://123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_https(self):
		Unit1 = self.crawle.filter_Url('https//123456')
		Unit2 = 'https//123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_HTTP(self):
		Unit1 = self.crawle.filter_Url('HTTP://123456')
		Unit2 = 'HTTP://123456'
		self.assertEqual(Unit1,Unit2)

	def test_filter_Url_http(self):
		Unit1 = self.crawle.filter_Url('http://123456')
		Unit2 = 'http://123456'
		self.assertEqual(Unit1,Unit2)

	#def test_findUrl(self):
	#	self.assertEqual(self.crawle.getHtmlCode(),self.crawle.htmlCode)

	#def test_printpath(self):
	#	saved_stdout = sys.stdout
	#	try:
	#		out = StringIO()
	#		sys.stdout = out
	#		self.crawle.printpath()
	#		output = out.getvalue().strip()
	#		assert output == 'http://www.nchu.edu.tw/\n["news.php?type=1&id=1","&page=0"\n{"pattern":"<font color="#999999">(.+?)</font>"}http://www.nchu.edu.tw/news.php?type=1&id=1&page=0"'
	#	finally:
	#		sys.stdout = saved_stdout





if __name__ == '__main__':
	#unittest.main()

	suite = unittest.TestLoader().loadTestsFromTestCase(TestCrawle)
	unittest.TextTestRunner(verbosity=2).run(suite)
