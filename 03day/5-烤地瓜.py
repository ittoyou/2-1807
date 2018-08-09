import random
class DiGua():
	def __init__(self):
		self.status = '生的'
		self.times = 0
		self.zl = []#装佐料
	def __str__(self):
		msg = '我烤的程度是%s'%self.status
		return msg+str(self.zl)
	def cook(self,time):
		self.times +=time
		if self.times >= 1 and self.times < 3:
			self.status = '生的'
		elif self.times >= 3 and self.times < 5:
			self.status = '半生不熟'
		elif self.times >= 5 and self.times < 8:
			self.stadus = '八分熟'
		elif self.times >= 8 and self.times < 12:
			self.status = '熟了'
		elif self.times >= 12:
			self.status = '烤焦了'
	def addzl(self,t):
		self.zl.append(t)
list = ['盐','糖','孜然','黑胡椒','油','味精']
digua = DiGua()
for i in range(5):
	digua.cook(random.randint(1,4))
	zl = random.choice(list)
	list.remove(zl)
	digua.addzl(zl)
	print(digua)
#digua = DiGua()
#digua.cook()
