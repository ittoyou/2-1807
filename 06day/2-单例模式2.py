class Son():
	__instance = None
	__flag = False
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		if Son.__flag == False:
			self.name = name
			Son.__flag = True

wife = Son('小红')
print(id(wife))
wife1 =Son('小丽')
print(id(wife1))
print(wife.name)
print(wife1.name)			
