class Dog():
	def __init__(self,name,food,wark):
		self.name = name
		self.food = food
		self.wark = wark
	def __str__(self):
		msg = '我的名字是%s,我的食物是%s,我的叫声是%s'%(self.name,self.food,self.wark)
		return msg
hashiqi = Dog('哈士奇','狗粮','汪汪汪')	
print(hashiqi)
xiaotianquan = Dog('哮天犬','二氧化碳','狂叫')
print(xiaotianquan)		


