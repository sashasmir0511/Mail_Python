import unittest
from MyMatrix import MyMatrix

class TestMyMatrix(unittest.TestCase):

	def testMath(self):
		a = MyMatrix([[1,1,1],[2,2,2],[3,3,3]])
		b = MyMatrix([[2,3,4],[3,4,2],[4,3,2]])
		self.assertEqual((a * b).lst, [[9, 10, 8], [18, 20, 16], [27, 30, 24]])
		self.assertEqual((b * a).lst, [[20, 20, 20], [17, 17, 17], [16, 16, 16]])
		self.assertEqual((a * 2).lst, [[2, 2, 2], [4, 4, 4], [6, 6, 6]])
		self.assertEqual((a + b).lst, [[3, 4, 5], [5, 6, 4], [7, 6, 5]])
		a.transpose()
		self.assertEqual(a.lst, [[1, 2, 3], [1, 2, 3], [1, 2, 3]])
		self.assertEqual(b.find_elem(5), False)
		self.assertEqual(b.find_elem(3), True)
		self.assertEqual(b[(1,1)], 4)
		self.assertEqual((a / 2).lst, [[0.5, 1.0, 1.5], [0.5, 1.0, 1.5], [0.5, 1.0, 1.5]])
		self.assertEqual((a % 2).lst, [[1, 0, 1], [1, 0, 1], [1, 0, 1]])
		self.assertEqual((a // 2).lst, [[0, 1, 1], [0, 1, 1], [0, 1, 1]])

if __name__ == '__name__':
	unittest.main()