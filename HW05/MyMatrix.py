from typing import List
from Cython_mul import Cython_mul

class MyMatrix:
	"""
	MyMatrix
	\mmm
	n000
	n123
	"""
	def __init__(self, lst: List[List[int]]) -> None:
		self.len_n = len(lst)
		self.len_m = len(lst[0])
		self.lst = [0] * self.len_n
		for i in range(self.len_n):
			#self.lst[i] = lst[i].copy()
			self.lst[i] = [0] * self.len_m
			for j in range(self.len_m):
				try:
					self.lst[i][j] = lst[i][j]
				except IndexError:
					print("This in not matrix") #Ask a Question.
		
	def __str__(self) -> str:
		str_matrix = ""
		for i in range(self.len_n):
			for j in range(self.len_m):
				str_matrix += str(self.lst[i][j]) + "\t"
			str_matrix += '\n'
		return str_matrix
	
	def __repr__(self) -> str:
		return f"MyMatrix({self.lst})"
	
	def __add__(self, b):
		if (self.len_n != b.len_n) or (self.len_m != b.len_m):
			return self
		lst = [0] * self.len_n
		for i in range(self.len_n):
			lst[i] = [0] * self.len_m
			for j in range(self.len_m):
				try:
					lst[i][j] = self.lst[i][j] + b.lst[i][j]
				except TypeError: # str + int = 0
					lst[i][j] = 0
		return MyMatrix(lst)
	
	def __mul__(self, b):
		lst = [0] * self.len_n
		if type(b) == MyMatrix: #isinstance
			if self.len_m == b.len_n:
				for i in range(self.len_n):
					lst[i] = [0] * b.len_m
					for j in range(b.len_m):
						s = 0
						for z in range(self.len_m):
							s += self.lst[i][z] * b.lst[z][j]
						lst[i][j] = s
				return MyMatrix(lst)
			else:
				return self #error
		elif type(b) == int: #isinstance
			for i in range(self.len_n):
				lst[i] = [0] * self.len_m
				for j in range(self.len_m):
					lst[i][j] = self.lst[i][j] * b
			return MyMatrix(lst)
		else:
			return self
	
	def C_mul(self, b):
		if self.len_m == b.len_n:
			return MyMatrix(Cython_mul(self.lst, b.lst, tuple([self.len_n, self.len_m]), tuple([b.len_n, b.len_m])))
	
	def __truediv__(self, b: int):
		lst = [0] * self.len_n
		for i in range(self.len_n):
			lst[i] = [0] * self.len_m
			for j in range(self.len_m):
				lst[i][j] = self.lst[i][j] / b
		return MyMatrix(lst)
	
	def __floordiv__(self, b: int):
		lst = [0] * self.len_n
		for i in range(self.len_n):
			lst[i] = [0] * self.len_m
			for j in range(self.len_m):
				lst[i][j] = self.lst[i][j] // b
		return MyMatrix(lst)
	
	def __mod__(self, b: int):
		lst = [0] * self.len_n
		for i in range(self.len_n):
			lst[i] = [0] * self.len_m
			for j in range(self.len_m):
				lst[i][j] = self.lst[i][j] % b
		return MyMatrix(lst)
	
	def transpose(self) -> None:
		lst = [0] * self.len_m
		for i in range(self.len_m):
			lst[i] = [0] * self.len_n
			for j in range(self.len_n):
				lst[i][j] = self.lst[j][i]
		self.len_n, self.len_m = self.len_m, self.len_n
		self.lst = lst
	
	def find_elem(self, f: int) -> bool:
		for i in range(self.len_n):
			for j in range(self.len_m):
				if (self.lst[i][j] == f):
					return True
		return False
	
	def __getitem__(self, tp: tuple) -> int:
		return self.lst[tp[0]][tp[1]]


if __name__ == '__main__':
	a = MyMatrix([[1,2,3],[1,2,4],[1,2,3]])
	b = MyMatrix([[2,4,5],[9,6,2],[8,1,4]])
	print(a * b)