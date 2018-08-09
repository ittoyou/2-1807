import os
dir_name = input('请输入要批量重命名的文件夹名字')
files = os.listdir(dir_name)
os.chdir(dir_name)
print(os.getcwd())

for i in files:
	position = i.rfind('.')
	newname = i[:position]+'-腾讯出品'+i[position:]
	os.rename(i,newname)

'''
for i in files:
	position = i.rfind('.')
	new_name = i[:position]+'-腾讯出品'+i[position:]
	old_name = dir_name+'/'+i
	new_name = dir_name+'/'+new_name
	os.rename(old_name,new_name)
'''
