from libc.stdlib cimport malloc,free
import numpy as np

cdef class CMatrix:
	
	cdef public int N
	cdef public int M
	cdef public int[:, :] matrix

	def __init__(self, lst):
		self.N = len(lst)
		self.M = len(lst[0])
		
		self.matrix = np.zeros((self.N, self.M), dtype=np.int32)
		for i in range(self.N):
			#self.matrix[i] = <int *>malloc(self.M * sizeof(int))
			for j in range(self.M):
				self.matrix[i, j] = lst[i][j]


	def __mul__(self, b):
		cdef int s = 0
		cdef int[:, :]lst = np.zeros((self.N, self.M), dtype=np.int32)
		if self.M == b.N:
			for i in range(self.N):
				for j in range(b.M):
					s = 0
					for z in range(self.M):
						s += self.matrix[i][z] * b.matrix[z][j]
					lst[i][j] = s
			return  CMatrix(lst)
		else:
			return self
		

	def __str__(self):
		str_matrix = ""
		for i in range(self.N):
			for j in range(self.M):
				str_matrix += str(self.matrix[i][j]) + "\t"
			str_matrix += '\n'
		return str_matrix

if __name__ == '__main__':
	a = CMatrix([[1,2,3],[1,2,4],[1,2,3]])
	b = CMatrix([[2,4,5],[9,6,2],[8,1,4]])
	print(a * b)