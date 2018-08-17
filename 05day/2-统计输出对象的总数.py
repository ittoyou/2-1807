class Cellphone():
	count = 0
	def __init__(self,name,color,type):
		Cellphone.count+=1
		self.name = name
		self.color = color
		self.type = type
	def call(self):
		print('打电话')
xiaomi = Cellphone('小米','红色','xm05')
xiaomi1 = Cellphone('小米','黑色','xm05')
xiaomi2 = Cellphone('小米','银灰色','xm05')
print(Cellphone.count)

