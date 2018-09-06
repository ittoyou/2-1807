def w(typ):
	def w1(fun):
		def inner(*args,**kwargs):
			return fun(*args,**kwargs)
		return inner
	return w1
