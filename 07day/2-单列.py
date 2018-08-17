'''
class Son():
	__instance = None
	__flag = False
	def __init__(self,name):
		if Son.__flag == False:
			self.name = name
			Son.__flag = True
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
gf = Son('小琼')
print(id(gf))
gf1 = Son('小露')
print(id(gf1))
print(gf.name)
print(gf1.name)
'''
class Dog():
	__instance = None
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		self.name = name
dog1 = Dog('小明')
print(id(dog1))

dog2 = Dog('小红')
print(id(dog2))


