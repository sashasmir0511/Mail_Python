class PositiveInt:

	def __get__(self, instance, owner):
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value, int):
			raise TypeError('Type not int')
		if value < 0:
			raise ValueError('Cannot be negative.')
		instance.__dict__[self.name] = value

	def __set_name__(self, owner, name):
		self.name = name

class StrUpper:

	def __get__(self, instance, owner):
		return instance.__dict__[self.name]

	def __set__(self, instance, value):
		if not isinstance(value, str):
			raise TypeError('Type not str')
		instance.__dict__[self.name] = value.upper()

	def __set_name__(self, owner, name):
		self.name = name
