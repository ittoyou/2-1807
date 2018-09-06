from threading import Thread
import time
def saysorry():
	print('领导,我错了')
	time.sleep(1)
for i in range(5):
	#t = Thread(target=saysorry)
	#t.start()
	saysorry()
