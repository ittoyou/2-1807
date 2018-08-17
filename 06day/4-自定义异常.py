class ShowError(Exception):
	def __init__(self,name):
		self.name = name
		
class InputManager():
	def my_input(self):
		self.name = input('请输入名字')
		try:
			if self.name == '老王':
				raise ShowError(self.name)
		except ShowError as ret:
			print('输入%s就报错'%ret.name)
		else:
			print('无异常')
a = InputManager()
a.my_input()

