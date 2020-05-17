import unittest
from MaxHeap import MaxHeap
from Cache import LRUCache, LFUCache, LRUCache_t
from MedianFinder import MedianFinder


class	TestMaxHeap(unittest.TestCase):
	
	def testheapify(self):
		lst = [10, 5, 3, -2, 11]
		heap = MaxHeap()
		heap.heapify(lst)
		self.assertEqual(heap.heap, [11, 10, 5, 3, -2])
	
	def testlen(self):
		lst = [10, 5, 3, -2, 11]
		heap = MaxHeap()
		heap.heapify(lst)
		self.assertEqual(len(heap), 5)
	
	def testpush(self):
		heap = MaxHeap()
		heap.push(10)
		heap.push(-4)
		heap.push(5)
		self.assertEqual(heap.heap, [10, 5, -4])
		
	def testpop(self):
		heap = MaxHeap()
		heap.push(10)
		heap.push(-4)
		heap.push(5)
		self.assertEqual(heap.pop(), 10)
		self.assertEqual(heap.pop(), 5)
		self.assertEqual(heap.pop(), -4)


class	TestLRUCache(unittest.TestCase):

	def testinit(self):
		cache = LRUCache()
		cache.set("Smirnov", "Sasha")
		cache.set('Jesse', 'Pinkman')
		cache.set('Walter', 'White')
		self.assertEqual(cache.get('Jesse'), 'Pinkman')
		cache.set('Jesse', 'James')
		self.assertEqual(cache.get('Jesse'), 'James')
		cache.delete('Walter')
		self.assertEqual(cache.get('Walter'), '')

	def testoverflow(self):
		cache = LRUCache(3)
		cache.set("Smirnov", "Sasha")
		cache.set('Jesse', 'Pinkman')
		cache.set('Walter', 'White')
		self.assertEqual(cache.get('Smirnov'), 'Sasha')
		cache.set('Python', 'Mail')
		self.assertEqual(cache.get('Smirnov'), '')


class	TestLRUCache_t(unittest.TestCase):

	def testinit(self):
		cache = LRUCache_t()
		cache.set("Smirnov", "Sasha")
		cache.set('Jesse', 'Pinkman')
		cache.set('Walter', 'White')
		self.assertEqual(cache.get('Jesse'), 'Pinkman')
		cache.set('Jesse', 'James')
		self.assertEqual(cache.get('Jesse'), 'James')
		cache.delete('Walter')
		self.assertEqual(cache.get('Walter'), '')

	def testoverflow(self):
		cache = LRUCache_t(3)
		cache.set("Smirnov", "Sasha")
		cache.set('Jesse', 'Pinkman')
		cache.set('Walter', 'White')
		self.assertEqual(cache.get('Smirnov'), 'Sasha')
		cache.set('Python', 'Mail')
		self.assertEqual(cache.get('Jesse'), '')


class	TestLFUCache(unittest.TestCase):

	def testinit(self):
		cache = LFUCache()
		cache.set("Smirnov", "Sasha")
		cache.set('Jesse', 'Pinkman')
		cache.set('Walter', 'White')
		self.assertEqual(cache.get('Jesse'), 'Pinkman')
		cache.set('Jesse', 'James')
		self.assertEqual(cache.get('Jesse'), 'James')
		cache.delete('Walter')
		self.assertEqual(cache.get('Walter'), '')

	def testoverflow(self):
		cache = LFUCache(3)
		cache.set("Smirnov", "Sasha")
		cache.set('Jesse', 'Pinkman')
		cache.set('Walter', 'White')
		self.assertEqual(cache.get('Smirnov'), 'Sasha')
		cache.set('Python', 'Mail')
		self.assertEqual(cache.get('Smirnov'), 'Sasha')
		self.assertEqual(cache.get('Jesse'), '')

class	TestMedianFinder(unittest.TestCase):
	def testfindMedian(self):
		obj = MedianFinder()
		obj.paste([1, 34, 45, 5, 23])
		self.assertEqual(obj.findMedian(), 23)
		obj.addNum(2)
		self.assertEqual(obj.findMedian(), 14.0)

if __name__ == '__main__':
	unittest.main()