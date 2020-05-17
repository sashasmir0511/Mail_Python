import unittest
from unittest.mock import patch
from hw06_prof import func

class Testfunc(unittest.TestCase):

	def test1(self):
		self.assertEqual([0], func([1]))
		self.assertEqual([2,1], func([1,2]))
		self.assertEqual([24,12,8,6], func([1,2,3,4]))
		self.assertEqual([24, 0,0,0], func([0,2,3,4]))


if __name__ == '__main__':
	unittest.main()