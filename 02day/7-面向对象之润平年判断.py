class Tool:
	def judge(self):
		year = int(input('请输入一个年份:'))
		if(year%4 == 0 and year%100 != 0)or(year%400 == 0):
			print('闰年')
		else:
			print('平年')

t = Tool()
t.judge()

