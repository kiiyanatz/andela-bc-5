def super_sum(*args):
	total = 0
	for i in args:
		# Check if two numbers
		if isinstance(i, int):
			total = total + i
		# Check if list is passed
		elif isinstance(i, list):
			total = []
	return total

a, b, c, d = [1, 2], [2, 3], [3], [4, 10]
print super_sum(a, b)