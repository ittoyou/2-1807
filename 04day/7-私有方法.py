class QQ():
	def __openvip(self):
		print('成功开通会员')
	def checkqq(self,money):
		if money > 10:
			self.__openvip()
		else:
			print('开不了')
a = QQ()
a.checkqq(11)
a1 = QQ()
a1.checkqq(8)
