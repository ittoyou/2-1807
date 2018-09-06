#1.将时间转化成时间戳
import time
dt = '2018-8-20 17:15:20'
#转换成时间数组
timeArray = time.strptime(dt, '%Y-%m-%d %H:%M:%S')
#转换成时间戳
timestamp = time.mktime(timeArray)
print(timestamp)

#2.将时间戳转化成时间
timestamp = 1534756520
#转化成localtime
time_local = time.localtime(timestamp)
#转化成新的时间格式(2018-8-20 17:15:20)
dt = time.strftime('%Y-%m-%d %H:%M:%S',time_local)
print(dt)
