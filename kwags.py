def output(name, **kwargs):
	print 'name: ', name
	for i in kwargs.keys():
		print i, ": ", kwargs[i]

output('Angela', age=19, gender='F', loc='NBO')