class Dog():
	def __init__(self):
		self.name = ''
		self.__age = 0
	def setAge(self,age):
		if age >15 and age < 1:
			print('不符和实际')
		else:
			self.__age = age
	def getAge(self):
		return self.__age
ly = Dog()
ly.setAge(12)
print(ly.getAge())
	
