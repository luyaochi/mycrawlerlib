#!/usr/bin/python
# -*-coding:utf-8-*-

import unittest
import urllib

from type1 import crawl
from type1 import frontier
from type1 import crawler
from type1 import frontier

path = 'http://www.nchu.edu.tw/index1.php'

a = crawler(path)
print(a.path)
print(a.htmlCode_Decode)
print(a.htmlCode_Undecode)
a.getURL()



print('show frontier List',a.show_frontier())
print('show first frontier',a.show_first_frontier())
print('len',a.len_frontier())
