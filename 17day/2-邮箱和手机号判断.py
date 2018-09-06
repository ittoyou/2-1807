import re 
def checkphone(phone):
	ret = re.match('1[3456789]\d{9}$',phone)
	if phone:
		print('合法')
	else:
		print('不合法')
checkphone('13569837902')
	
