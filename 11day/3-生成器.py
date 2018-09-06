def fib():
	a,b = 0,1
	#print('---1---')
	for i in range(10):
		#print('---2---')
		yield b
		#print('---3---')
		a,b = b,a+b
#print(fib())
G = fib()
#print(next(G))
for i in G:
	print(i)
