'''
class Cat():
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
cat = Cat()
print(id(cat))
cat1 =Cat()
print(id(cat1))
'''



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
wife = Son('小慧')
print(id(wife))
wife1 = Son('小莉')
print(id(wife1))
print(wife.name)
print(wife1.name)

'''
class Son():
    __instance = None 
    __flag = False
    def __init__(self,name):
        if Son.__flag == False:
            self.name = name 
            Son.__flag = True

    def __new__(cls,*args,**kwargs):#重写
        if cls.__instance == None:
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

xifu = Son("小红")
print(id(xifu))

xifu1 = Son("小明")
print(id(xifu1))

print(xifu.name)
print(xifu1.name)
'''
