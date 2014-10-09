#!/usr/bin/python
# -*-coding:utf-8-*-

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
		if len(self.list_frontier) > 0:
			return self.list_frontier[0]
		return ''

	def len_frontier(self):
		return len(self.list_frontier)

