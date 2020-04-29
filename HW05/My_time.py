from random import randint
from timeit import timeit
from MyMatrix import MyMatrix
from C_mul import CMatrix
from datetime import datetime

def time_test():
	lst1 = [[randint(0, 100) for i in range(100)] for _ in range(100)]
	lst2 = [[randint(0, 100) for i in range(100)] for _ in range(100)]
	a = MyMatrix(lst1)
	b = MyMatrix(lst2)
	c = CMatrix(lst1)
	d = CMatrix(lst2)
	
	start_time = datetime.now()
	a * b
	print(f"Time Python is {datetime.now() - start_time}")

	start_time = datetime.now()
	a.C_mul(b)
	print(f"Time CPython is {datetime.now() - start_time}")

	start_time = datetime.now()
	c * d
	print(f"Time Cython is {datetime.now() - start_time}")

if __name__ == '__main__':
	time_test()