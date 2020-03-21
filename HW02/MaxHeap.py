from typing import List

class MaxHeap:
	def __init__(self) -> None:
		self.heap = []

	def push(self, val: int) -> None:
		i = 0
		while i < len(self.heap) and val <= self.heap[i]:
			i += 1
		self.heap.insert(i, val)

	def pop(self) -> int:
		return(self.heap.pop(0))

	def heapify(self, iterable: List[int]) -> None:
		for value in iterable:
			self.push(value)
			
	def __len__(self) -> int:
		return(len(self.heap))