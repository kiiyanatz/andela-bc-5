def my_sum(*args):
	total = 0
	for i in args:
		total += i
	return total
	
print my_sum(1, 33)