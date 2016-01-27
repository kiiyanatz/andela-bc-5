class Vehicle(object):
	def __init__(self, engine, **kwargs):
		self.engine = engine
		for key, value in kwargs.items():
			setattr(self, key, value)

	def set_color(self, color):
		self.color = color

	def set_speed(self, speed):
		self.speed = speed

class Car(Vehicle):
	"""docstring for Car"""
	def __init__(self, engine_type, car_category, **kwargs):
		super(Car, self).__init__(engine_type, **kwargs)
		self.car_category = car_category
		self.doors = 5
		self.wheels = 4
		self.set_color("Red")

ax = Car("5000cc", "Saloon", max_speed=220, color="red")
print ax.engine
print ax.color		

