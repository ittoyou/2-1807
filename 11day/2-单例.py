class Dog():
	__instance = None
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
dog1 = Dog('xiaoli')
dog2 = Dog('xiaogao')
print(id(dog1))
print(id(dog2))


