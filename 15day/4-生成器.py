def test():
	a,b = 0,1
	for i in range(10):
		a,b = b,a+b
		yield b
t = test()
for i in t:
	print(i)
