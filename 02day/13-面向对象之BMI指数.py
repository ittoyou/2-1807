class Tool():
	def judge(self):
		weight = float(input('请输入体重(kg)'))
		height = float(input('请输入身高(m)'))
		bmi = weight/(height**2)
		print(bmi)
		if bmi < 18:
			print('过轻')
		elif bmi >= 18 and bmi < 25:
			print('正常')
		elif bmi >= 25 and bmi < 28:
			print('过重')
		elif bmi >= 28 and bmi < 32:
			print('肥胖')
		elif bmi >= 32:
			print('严重肥胖')
jd = Tool()
jd.judge()
