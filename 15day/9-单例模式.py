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
dog1 = Dog('xiaohu')
print(id(dog1))
print(dog1.name)
dog2 = Dog('xiaochen')
print(id(dog2))
print(dog2.name)
