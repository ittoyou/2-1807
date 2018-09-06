from socket import *
#创建一个udp套接字
s = socket(AF_INET,SOCK_DGRAM)
#对方ip 端口
s.sendto('秋天到了,收获的季节'.encode('gb2312'),('192.168.43.145',8080))
s.close()
