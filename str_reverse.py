def reverse(s):
	return s[::-1]

def reversex(x):
	x = list(x)
	for i in range(len(x)//2):
		temp = x[i] # Holds letter n
		x[i] = x[len(x) - 1 -i] # first index = last index
		x[len(x) - 1 -i]= temp
	return x

print " ".join(reversex("hello"))
