class Tool:
	def beifen(self): 
		name = input('请输入要备份的文件名字(加上后缀名)')
		f = open(name,'r')
		#content = f.read()
		position = name.rfind('.')
		newname = name[:position]+'备份'+name[position:]
		f1 = open(newname,'w')
		while True:
			content = f.read(1024)
			if len(content) == 0:
				break
			f1.write(content)
		f.close()
		f1.close()
bf = Tool()
bf.beifen()
