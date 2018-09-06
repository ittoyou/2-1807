import pickle
import os
class Manger():
    def __init__(self):
        self.name = "教师管理系统v1.0"
        self.list = []

    def add(self,teacher):
        self.list.append(stu)
        #写入日志
        self.writerizhi("几点掉了add方法")

    def find(self):
        #写入日志AA
        self.writerizhi("几点掉了find方法")
        pass

    def delete(self):
        pass

    def change(self):
        pass

    def writerizhi(self,str):
        """
        写文件
        """


class Teacher():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
m = Manger()
while True:
    name = input("请输入教师名字")
    age = input("请学生教师年龄")
    sex = input("请输入教师性别")
    stu = Teacher(name,age,sex)
    m.add(teacher)
