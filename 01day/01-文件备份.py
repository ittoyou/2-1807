name = input('请输入要备份的文件名字(加上后缀名)')
f = open(name,'r')
content = f.read()
position = name.rfind('.')
newname = name[:position]+'备份'+name[position:]
f1 = open(newname,'w')
f1.write(content)
f.close()
f1.close()
'''
name = input("请输入要备份的文件名字")
f = open(name,"r")
while True:
	if f.read(1024) == "":
		break
content = f.read(1024)
p = name.rfind(".")
f1 = open(name[:p]+"back"+name[p:],"w")
f1.write(content)
f.close()
f1.close()
'''
