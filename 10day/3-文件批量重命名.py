import os
class Tool():
	def operation(self):
		dir_name = input('请输入要批量重命名的文件夹名字:')
		files = os.listdir(dir_name)
		os.chdir(dir_name)
		for i in files:
			position = i.rfind('.')
			newname = i[:position] +'---经典'+i[position:]
			os.rename(i,newname)
t = Tool()
t.operation()
		
