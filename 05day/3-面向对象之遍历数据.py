class Tool():
	def __init__(self):
		self.list = [{"北京":{"面积":"1000平","人口":"200w"},"上海":{"面积":"600平","人口":"150w"}}]
	def operation(self):
		for i in self.list:
			for k,v in i.items():
				for j,l in v.items():
					print(k,j,l)
t = Tool()
t.operation()
