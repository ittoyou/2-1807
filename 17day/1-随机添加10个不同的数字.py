import random
list = []
if __name__ == '__main__':
	while len(list) < 10 :
		number = random.randint(1,100)
		if number in list:
			print("重复了%d"%number)
			continue
		list.append(number)
list.sort()
print(list)
'''
for i in list:
	print('序号:%s 值:%s'%(list.index(i)+1,i))
for i in range(len(list)):
	print('序号:%s 值:%s'%(i+1,list[i]))
for i,val in enumerate(list):
	print('序号:%s 值:%s'%(i+1,val))
'''
for i in list:
	position = int(input('请输入一个索引:'))
	print('索引%s的值:%s'%(list.index(i)+1,i))


