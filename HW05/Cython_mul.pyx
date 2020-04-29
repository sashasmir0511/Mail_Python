
def Cython_mul(list a, list b, tuple t_a, tuple t_b):
	cdef list lst
	cdef int i
	cdef int j
	cdef int z
	cdef int s
	lst = [0] * t_a[0]
	for i in range(t_a[0]):
		lst[i] = [0] * t_b[1]
		for j in range(t_b[1]):
			s = 0
			for z in range(t_a[1]):
				s += a[i][z] * b[z][j]
			lst[i][j] = s
	return lst

if __name__ == '__main__':
	Cython_mul([[1,1],[1,1]],[[2,2],[3,3]],(2,2),(2,2))