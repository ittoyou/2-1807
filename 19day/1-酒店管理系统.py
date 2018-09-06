import time
def writeLog(msg):
    with open("log.txt","a") as f:
        f.write(msg)
def w1(fun):
    def inner(*args,**kwargs):
        msg  = str(fun)+str(time.ctime())+"\n"
        writeLog(msg)
        fun(*args,**kwargs)
    return inner
class Hotel():
	def __init__(self):
		self.name = name
		self.list = []
		self.money = money
	@w1
	def inHome(self,person):
		person.time = int(time.time())
		person.islive = True
		self.list.append(person)
	@w1
	def outHome(self,name):
		for person in self.list:
			if person.name == name:
				person.islive = False
				endtime = int(time.time())
				out_money = (endtime - person.time)*10
				print("花了%.02f"%out_money)
				self.money+=out_money
				break
	@w1
	def tongji():
		count = 0
		for person in self.list:
			if not person.islive:
				count+=1
			print("今天一共入住%d人,离店%d人,收入%.02f"%(len(self.list),count,self.money))
class Person():
	def __init__(self):
		self.name = name
		self.age = age
		self.sex = sex
	def setCard(self,card):
		if len(card) == 3:
			self.card = card
	def isPhone():
		if	len(isPhone) == 11 and startswith(1):
			print('输入成功') 
		else:
			print('输入有误,请重新输入')
hzl = Hotel('好再来')
while True:
	print('-----欢迎来到酒店管理系统-----')
	num = int(input('1:入住 2:离店 3: 统计 4: 退出'))
	if num == 1:
		name = input('请输入姓名:')
		card = input("请输入身份证:")
		ll = Person(name)
		ll.setCard(card)
		hzl.inHome(ll)
	elif num == 2:
		name = input('请输入姓名:')
		hzl.outHome(name)
	elif num == 3:
		hzl.tongji()
	elif num == 4:
		exit()

