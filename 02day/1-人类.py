class Person:
	def readBook(self):
		print('读书')
	def listenMusic(self):
		print('听音乐')
	def watchMovie(self):
		print('看电影')
	def introduce(self):
		print('我的年龄是%d岁,我的身高是%d厘米,我的体重是%d千克'%(self.age,self.height,self.weight))
xiaoming = Person()
xiaoming.readBook()
xiaoming.listenMusic()
xiaoming.watchMovie()
xiaoming.age = 21
xiaoming.height = 160
xiaoming.weight = 60
xiaoming.introduce()
