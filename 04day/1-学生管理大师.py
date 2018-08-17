class Student():
	def __init__(self,name,sex):
		self.name = name
		self.sex = sex
	def listen(self):
		print('上课')
	def __str__(self):
		return '我的名字是%s,性别是%s'%(self.name,self.sex)
class Manager():
	def __init__(self):
		self.list = []
	def add(self,student):
		self.list.append(student)
		self.save()
	def remove(self):
		pass
	def update(self):
		pass
	def find(self,name):
		for student in self.list:
			if student.name == name:
				print('我的名字是%s,性别是%s'%(student.name,student.sex))
	def save(self):
		with open('data.bat','w') as f:
			f.write(str(self.list))
	def read(self):
		pass
	def print_student(self):
		for student in self.list:
			print('我的名字是%s,性别是%s'%(student.name,student.sex))
class Menu():#菜单类
    
    def __init__(self):
        self.m = Manager()

    def print_men(self):
        print("欢迎来学生管理系统")
        while True:
            fun = int(input("请选择功能"))
            if fun == 1:
                name = input("请输入学生名字")
                sex = input("请输入学生性别")
                s = Student(name,sex)
                self.m.add(s)
            elif fun == 2:
                name = input("请输入你查找学生姓名")
                self.m.find(name)

menu = Menu()
menu.print_men()

