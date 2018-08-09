class Tool():
	def table(self):
		for i in range(1,10):
			for j in range(1,i+1):
				print('%d*%d=%2d'%(j,i,j*i),end=' ')
			print(' ')
t = Tool()
t.table()
