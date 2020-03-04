class MyList(list):
	def __sub__(self, b):
		res = MyList()
		len_res = len(self) if len(self) > len(b) else len(b)
		for _ in range(len_res):
			res.append(0)
		for i in range(len(self)):
			res[i] = self[i]
		for i in range(len(b)):
			res[i] -= b[i]
		return (res)

	def __add__(self, b):	
		res = MyList()
		len_res = len(self) if len(self) > len(b) else len(b)
		for _ in range(len_res):
			res.append(0)
		for i in range(len(self)):
			res[i] = self[i]
		for i in range(len(b)):
			res[i] += b[i]
		return (res)

	def sum(self):
		sum_self = 0
		for i in range(len(self)):
			sum_self += self[i]
		return (sum_self)

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



print(issubclass(MyList, list))

a = MyList()
a.append(10)
a.append(10)
a.append(10)

b = MyList()
b.append('a')
b.append(1)
b.append(2)
b.append(3)

c = a - b
print(a, b, c)
c = a + b
print(a, b, c)
print(sum(a), sum(b))
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)
print(a == b)