class Student():
	count = 0
	@staticmethod
	def listen():
		print('上课学习')
	def __init__(self,name):
		self.name = name
		Student.count += 1
s1 = Student('小李')
s2 = Student('小张')
s3 = Student('小刘')
print(Student.count)
