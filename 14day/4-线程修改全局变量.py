from threading import Thread
import time
num = 0
flag = 1
def work1():
	global num,flag
	if flag == 1:
		for i in range(1000000):
			num+=1
		print('Thread-1')
		print(num)
		flag = 2
def work2():
	global num
	while True:
		if flag == 2:
			for i in range(1000000):
				num+=1
			print('Thread-2')
			print(num)
			break
t1 = Thread(target=work1)
t1.start()
#t1.join()
t2 = Thread(target=work2)
t2.start()

