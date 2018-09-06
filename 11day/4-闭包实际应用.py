def count(x,y):
	def count1(z):
		return x*z + y
	return count1
count2 = count(2,3)
print(count2(2))
print(count2(3))
print(count2(4))

