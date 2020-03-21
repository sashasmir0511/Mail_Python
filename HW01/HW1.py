class MyList(list):
	def __sub__(self, b):
		res = MyList()
		len_res = len(self) if len(self) > len(b) else len(b)
		for _ in range(len_res):
			res.append(0)
		for i in range(len(self)):
			res[i] = self[i]
		try:
			for i in range(len(b)):
				res[i] -= b[i]
		except TypeError:
			print("Список содержит элементы неправильного типа")
		return (res)

	def __add__(self, b):	
		res = MyList()
		len_res = len(self) if len(self) > len(b) else len(b)
		for _ in range(len_res):
			res.append(0)
		for i in range(len(self)):
			res[i] = self[i]
		try:
			for i in range(len(b)):
				res[i] += b[i]
		except TypeError:
			print("Список содержит элементы неправильного типа")
		return (res)

	def __lt__(self, b):
		return (sum(self) < sum(b))

	def __le__(self, b):
		return (sum(self) <= sum(b))

	def __eq__(self, b):
		return(sum(self) == sum(b))

	def __ne__(self, b):
		return(sum(self) != sum(b))

	def __gt__(self, b):
		return(sum(self) > sum(b))

	def __ge__(self, b):
		return(sum(self) >= sum(b))

class MyMiniBank():
	'''
	Класс для подсчёта суммы в разных валютах.
	Были выбраны следующие валюты:
	RUB, EUR, USD, Gram (криптовалюта от Telegram), BYN (Белорусский рубль).
	По умолчанию используется валюта RUB.
	Переводится по следующим правилам:
		1 BYN = 30.58 RUB
		1 EUR = 77,38 RUB
		1 USD = 68,56 RUB
		1 Gram = 1 000 000 000 RUB (Потому что можем)
	'''
	def __init__(self, money, currency = None):
		try:
			if (currency == "RUB" or currency == "BYN" or currency == "EUR" 
					or currency == "Gram" or currency == "USD" or currency is None) and money >= 0:
				self.money = money
				self.currency = currency
			else:
				raise ValueError
		except ValueError:
			print("Error")

	def __str__(self):
		return ("In your account {a} {b}".format(a=self.money, b=self.currency))
	
	def __repr__(self):
		return ("MyMiniBank({a},{b})".format(a=self.money, b=self.currency))
	
	def __add__(self, b):
		res = MyMiniBank(self.money, self.currency)

		if self.currency is None:
			res.money += b.money
			res.currency = b.currency
			return(res)
		if self.currency == b.currency:
			res.money += b.money
		else :
			res.money += b.exchange(self.currency)
		return(res)

	def exchange(self, current):
		switcher = {
			"RUB": 1,
			"EUR": 77.38,
			"USD": 68.56,
			"BYN": 30.58,
			"Gram": 1000000000,
		}
		return self.money * switcher.get(self.currency) / switcher.get(current)
