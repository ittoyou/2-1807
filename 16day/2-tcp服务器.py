from socket import *
#AF_INET ipv4
s =socket(AF_INET,SOCK_STREAM)
s.bind(('',1235))
s.listen(5)#监听最大客服端链接数
s1,address = s.accept()#等着接电话
msg = s1.recv(1024)#接收消息
print(msg.decode('gb2312'))
s1.send('你好'.encode('gb2312'))
s1.close()
s.close()

