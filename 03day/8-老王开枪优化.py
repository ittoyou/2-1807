import time
import random
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100
	def zhuangzidan(self,dj,zd):
		dj.addzidan(zd)
	def zhuangdanjia(self,dj,gun):
		gun.addDanJia(dj)
	def naqiang(self,gun):
		self.gun = gun
	def kaiqiang(self,diren):
		self.gun.kaihuo(diren)
	def diaoxue(self,hurt):
		self.hp -= hurt
		if self.hp <= 0:
			print('挂了')
		else:
			print('敌人%s还剩%d'%(self.name,self.hp))
class Gun():
	def __init__(self,name):
		self.name = name
		self.dj = None
	def addDanJia(self,dj):
		self.dj = dj
	def kaihuo(self,diren):
		zidan = self.dj.tanzidan()
		zidan.sharen(diren)
class DanJia():
	def __init__(self,count):
		self.count = count
		self.zds = []
	def addzidan(self,zd):
		self.zds.append(zd)
	def tanzidan(self):
		return self.zds.pop(0)
class ZiDan():
	def __init__(self,name,hurt):
		self.name = name
		self.hurt = hurt
	def sharen(self,diren):
		diren.diaoxue(self.hurt)
laowang = Person('老王')
print('老王出现了')
time.sleep(1)
ak47 = Gun('AK47')
print('出现一把AK47步枪')
time.sleep(1)
dj = DanJia(40)
print('装子弹中')
for i in range(40):
	zd = ZiDan('5.56',random.randint(1,100))
	laowang.zhuangzidan(dj,zd)
laowang.zhuangdanjia(dj,ak47)
time.sleep(3)
laowang.naqiang(ak47)
laoli = Person('老李')
for i in range(30):
	time.sleep(1)
	print('老王开枪')
	laowang.kaiqiang(laoli)


