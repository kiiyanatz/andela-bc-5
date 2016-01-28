class PrimeChecker(object):
	def __init__(self, number):
		if number == '' or number == ' ':
			number = '0'
		self.number = int(number)

	def is_prime(self):
		if self.number < 2:
			return False
		for i in range(2, self.number + 1):
			if i % 2 == 0:
				return True
		return False

checker = PrimeChecker()
print checker.is_prime()
print type(checker)

