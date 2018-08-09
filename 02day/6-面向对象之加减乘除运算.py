class Tool:
	def count(self):
		a = int(input('请输入一个a值:'))
		b = int(input('请输入一个b值:'))
		c = input('请输入+-*/:')
		if c == '+':
			c = a+b
			print('%d+%d=%d'%(a,b,c))
		elif c== '-':
			c = a-b
			print('%d-%d=%d'%(a,b,c))
		elif c == '*':
			c = a*b
			print('%d*%d=%d'%(a,b,c))
		elif c == '/':
			if b != 0:
				c = a/b
				print('%d/%d=%.02f'%(a,b,c))
			else:
				print('输入有误')
t = Tool()
t.count()

