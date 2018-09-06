from socket import *
#创建一个udp套接字
s = socket(AF_INET,SOCK_DGRAM)
while True:
	content = input('请输入内容:')
	s.sendto(content.encode('gb2312'),('192.168.43.145',8080))
	print('开始')
	msg = s.recvfrom(1024)
	print('结束')
	print(msg[0].decode('gb2312'),msg[1][0])
s.close()
