class Car():
	def __init__(self,name,color,size):
		self.name = name
		self.color = color
		self.size = size
	def __str__(self):
		msg = '我的名字是%s,我的颜色是%s,我的大小是%d'%(self.name,self.color,self.size)
		return msg
	def move(self):
		print('车会跑')
	def listen(self):
		print('车可以听音乐')
'''
	def introduce(self):
		print('我的名字是%s,我的颜色是%s,我的大小是%d'%(self.name,self.color,self.size))
'''
benchi = Car('奔驰','黑色',12)
benchi.move()
benchi.listen()
#benchi.introduce()
print(benchi)
