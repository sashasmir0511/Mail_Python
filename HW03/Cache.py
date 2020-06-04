from collections import OrderedDict
from Node import CacheNode, FreqNode
from datetime import datetime

class LRUCache:

	def __init__(self, capacity: int=10) -> None:
		self.max_length = capacity
		self.dict = OrderedDict()

	def get(self, key: str) -> str:
		return(self.dict.get(key, ""))

	def set(self, key: str, value: str) -> None:
		self.dict[key] = value
		if len(self.dict) > self.max_length:
			self.dict.popitem(last=False);

	def delete(self, key: str) -> None:
		self.dict.pop(key)


class LRUCache_t:

	def __init__(self, capacity: int=10) -> None:
		self.capacity = capacity
		self.dict_time = {}
		self.dict = {}

	def set(self, key: str, value: str) -> None:
		self.dict[key] = value
		self.dict_time[key] = datetime.now()
		if len(self.dict) > self.capacity:
			key = self.get_last_time()
			self.dict.pop(key)
			self.dict_time.pop(key)

	def get(self, key: str) -> str:
		result = self.dict.get(key, "")
		if result != "":
			self.dict_time[key] = datetime.now()
		return(result)

	# сделать за const
	def get_last_time(self) -> str:
		last_time = datetime.now()
		for i in self.dict_time.keys():
			if last_time > self.dict_time[i]:
				last_time = self.dict_time[i]
				key = i
		return key

	def delete(self, key: str) -> None:
		self.dict.pop(key)
		self.dict_time.pop(key)


class LFUCache:
	def __init__(self, capacity: int=10) -> None:
		self.capacity = capacity
		self.cache = {} # {key: cache_node}
		self.freq_link_head = None

	def get(self, key: str) -> str:
		if key in self.cache:
			cache_node = self.cache[key]
			freq_node = cache_node.freq_node
			value_node = cache_node.value
			self.move_forward(cache_node, freq_node)
			return value_node
		else:
			return ""
	
	def set(self, key: str, value: str) -> None:
		if key in self.cache:
			cache_node = self.cache[key]
			cache_node.value = value
			freq_node = cache_node.freq_node
			self.move_forward(cache_node, freq_node)
		else:
			if len(self.cache) >= self.capacity:
				self.dump_cache()
			self.create_cache(key, value)

	def move_forward(self, cache_node, freq_node):
		if freq_node.nxt is None or freq_node.nxt.freq != freq_node.freq + 1:
			target_freq_node = FreqNode(freq_node.freq + 1, None, None)
			target_empty = True
		else:
			target_freq_node = freq_node.nxt
			target_empty = False
		
		cache_node.free_myself()
		target_freq_node.append_cache_to_tail(cache_node)

		if target_empty:
			freq_node.insert_after_me(target_freq_node)

		if freq_node.count_caches() == 0:
			if self.freq_link_head == freq_node:
				self.freq_link_head = target_freq_node

			freq_node.remove()

	def dump_cache(self):
		head_freq_node = self.freq_link_head
		self.cache.pop(head_freq_node.cache_head.key)
		head_freq_node.pop_head_cache()

		if head_freq_node.count_caches() == 0:
			self.freq_link_head = head_freq_node.nxt
			head_freq_node.remove()

	def create_cache(self, key, value):
		cache_node = CacheNode(key, value)
		self.cache[key] = cache_node
		
		if self.freq_link_head is None or self.freq_link_head.freq != 0:
			new_freq_node = FreqNode(0)
			new_freq_node.append_cache_to_tail(cache_node)

			if self.freq_link_head is not None:
				self.freq_link_head.insert_before_me(new_freq_node)
			
			self.freq_link_head = new_freq_node
		else:
			self.freq_link_head.append_cache_to_tail(cache_node)

	def delete(self, key):
		self.cache.pop(key)
