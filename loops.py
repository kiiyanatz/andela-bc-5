ydef decrypt():
	garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
	print len(garbled)
	garbled = list(garbled)
	print len(garbled)
	for i in garbled:
		if i == 'X':
			garbled.remove(i)
	return "".join(garbled)

print decrypt()

