'''
date = '2018-08-17'

'''
def count_days(year,month,day):
	big_month = [1,3,5,7,8,10,12]
	small_month =[4,6,9,11]
	days = 0
	for i in range(1,month):
		if i in big_month:
			days+=31
		if i in small_month:
			days+=30
		if i == 2:
			if(i%4 == 0 and i%100 !=0) or (i%400==0):
				days+=29
			else:
				days+=28
	days+=day
	print("有%d天"%days)
date ="20180817"
year = int(date[0:4])
month = int(date[4:6])
day = int(date[6:])
count_days(year,month,day)
