class Flower():
	def __init__(self):
		self.__name = ''
		self.color = ''
			
	def setName(self,name):
		if len(name) > 5 or len(name) < 2:
			print('不合实际')
		else:
			self.__name = name
	def getName(self):
		return self.__name
hdl = Flower()
hdl.setName('蝴蝶兰')
print(hdl.getName())
hdl1 = Flower()
hdl1.setName('一株天山雪莲')	
print(hdl1.getName())	
