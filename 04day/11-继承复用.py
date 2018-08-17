class Plant():
	def __init__(self,name,color):
		self.name = name
		self.color = color
	def grow(self):
		pass
	def sleep(self):
		pass
class Flower(Plant):
	pass
class Shucai(Plant):
	pass
mg = Flower('玫瑰','蓝色')

bc = Shucai('白菜','绿色')

