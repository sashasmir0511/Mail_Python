from typing import List

class MedianFinder:

	def __init__(self):
		self.lst = []

	def addNum(self, num: int) -> None:
		i = 0
		while i < len(self.lst) and num <= self.lst[i]:
			i += 1
		self.lst.insert(i, num)

	def findMedian(self) -> float:
		len_lst = len(self.lst)
		if len_lst % 2 == 0:
			return (self.lst[len_lst // 2] + self.lst[len_lst // 2 - 1]) / 2
		else:
			return self.lst[len_lst // 2]

	def __len__(self) -> int:
		return len(self.lst)

	def paste(self, iterable: List[int]) -> None:
		for value in iterable:
			self.addNum(value)
