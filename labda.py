'''
def make_inc(n):
	return lambda x: x + n

y = make_inc(4)

print y(23)

'''

def is_even(n):
	return n % 2 == 0

l = [2, 10, 4, 5, 6, 11, 12]

new_list = filter(is_even, l)

print new_list