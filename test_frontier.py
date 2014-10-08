#!/usr/bin/python
# -*-coding:utf-8-*-

import unittest
import urllib

from type1 import frontier

path = 'http://www.nchu.edu.tw/index1.php'
#test frontier
class TestFrontier(unittest.TestCase):
	#test initialize variable
	def setUp(self):
		self.frontier = frontier(path)

	def test_init_frontier(self):
		self.frontier = frontier()
		Unit1 = [path]
		Unit2 = self.frontier.init_frontier(path)
		self.assertEqual(Unit1,Unit2)

	def test_list_frontier_none(self):
		#initialize
		self.frontier = frontier()
		Unit1 = []
		Unit2 = self.frontier.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_list_frontier_path(self):
		#initialize
		self.frontier = frontier(path)
		Unit1 = [path]
		Unit2 = self.frontier.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_show_frontier(self):
		Unit1 = self.frontier.show_frontier()
		Unit2 = self.frontier.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_add_frontier_notSamePath(self):
		self.frontier.add_frontier('secondPath')
		Unit1 = self.frontier.show_frontier()
		Unit2 = self.frontier.list_frontier
		self.assertEqual(Unit1,Unit2)

	def test_add_frontier_SamePath(self):
		self.frontier.add_frontier('Path')
		Unit1 = len(self.frontier.show_frontier())
		Unit2 = len(self.frontier.list_frontier)
		self.assertEqual(Unit1,Unit2)

	def test_del_frontier(self):
		self.frontier.add_frontier(path)
		self.frontier.add_frontier(path)
		Unit1 = len(self.frontier.show_frontier())
		self.frontier.del_frontier()
		Unit2 = len(self.frontier.show_frontier())
		self.assertEqual(Unit1,Unit2+1)

	def test_show_first_frontier(self):
		Unit1 = self.frontier.list_frontier[0]
		Unit2 = self.frontier.show_first_frontier()
		self.assertEqual(Unit1,Unit2)

	def test_len_frontier(self):
		Unit1 = len(self.frontier.show_frontier())
		Unit2 = self.frontier.len_frontier()
		self.assertEqual(Unit1,Unit2)


if __name__ == '__main__':

	suite = unittest.TestLoader().loadTestsFromTestCase(TestFrontier)
	unittest.TextTestRunner(verbosity=2).run(suite)