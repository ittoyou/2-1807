#coding=utf-8
try:
	print('test1')
	open('1.txt','r')
	print('test2')
except IOError:
	print('出错了')
