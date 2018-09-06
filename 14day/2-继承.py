class B():
	def handle(self):
		print('正在作业')
class A(B):
	def handle(self):
		print('作业中')
		#super().handle()
		#B.handle(self)
		super(A,self).handle()
a = A()
a.handle()
