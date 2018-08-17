class ATM():
	def __quqian(self):
		print('成功取款')
	def checkcard(self,money):
		if money >= 100:
			self.__quqian()
		else:
			print('取不了')
a = ATM()
a.checkcard(100)
a1 = ATM()
a.checkcard(50)
			
