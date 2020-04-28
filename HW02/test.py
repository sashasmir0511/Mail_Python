from HW1 import	MyList, MyMiniBank

a = MyList([3, 4, 10])

b = MyList([1, 3, 6, 8])

print("a + b", a + b)
print("a - b", a - b)
print("a > b: ", a > b)
print("a < b: ", a < b)


c = MyMiniBank(100, 'RUB')
d = MyMiniBank(200, 'EUR')
print(c)
print(d)
print(c.__repr__())

print(c + d)
