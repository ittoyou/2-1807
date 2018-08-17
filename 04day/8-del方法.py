class Dog():
	def __init__(self):
		print('__init__方法')
	def __str__(self):
		print('__str__方法')
	def __del__(self):
		print('__del__方法')
dog = Dog()
dog1 = dog
dog2 = dog
del dog
del dog1
print('结束')
