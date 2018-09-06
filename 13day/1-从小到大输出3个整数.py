'''
l = []
for i in range(3):
    x = int(input('请输入数字'))
    l.append(x) #这里用append()函数，意思是追加元素
    l.sort()
print(l)
'''

'''
def sort_int(a,b,c):
	l = [a,b,c]
	l.sort()
	return l
x,y,z = sort_int(100,10,1)
print(x,y,z)
'''

'''
import re
x, y, z = re.split(',| |，|  ', input('请输入3个数字，用逗号或空格隔开：'))
x, y, z = int(x), int(y), int(z)

maxNo = max(x, y, z)
minNo = min(x, y, z)
print(minNo, x+y+z-maxNo-minNo, maxNo)
'''
'''
#方法二  用re.split()得到3个字符型数字的列表，把字符转换为数字，排下序，然后 print()代码如下：
import re

lst = re.split(',| |，|  ', input('请输入3个数字，用逗号或空格隔开：'))
for i in range(len(lst)):
    lst[i] = int(lst[i])
lst.sort()
#print(lst)
for i in lst:
	print(i)
'''

x = int(input('please input x:'))  
y = int(input('please input y:'))  
z = int(input('please input z:'))  
if x > y :  
    x,y = y,x  
if x > z :  
    x, z = z, x  
if y > z :  
    y, z = z, y  
print(x,y,z) 

