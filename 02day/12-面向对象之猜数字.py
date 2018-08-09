class Tool():
	def judge(self):
		import random
		computer = random.randint(1,100)
		player = int(input('请选择一个数字'))
		if computer > player:
			print('你的数字小了')
		elif computer < player:
			print('你的数字大了')
		elif computer == player:
			print('你猜对了')
t = Tool()
t.judge()
