import cProfile
import pstats
import logging


def profile(func):
	def wrapper(*args, **kwargs):
		profile_name = func.__name__ + ".txt"
		prof = cProfile.Profile()
		result = prof.runcall(func, *args, **kwargs)
		prof.dump_stats(profile_name)
		return result
	return wrapper

@profile
def func(lst):
	len_lst = len(lst)
	if len_lst == 1:
		logging.debug('one element')
		logging.info('wtf')
		logging.warning('1\n')
		return [0]
	res_lst = [0] * len_lst
	for i in range(len_lst):
		res_i = 1
		for j in range(len_lst):
			if j != i:
				if isinstance(lst[j], int):
					res_i *= lst[j]
				else:
					logging.debug('Один элемент не число')
					logging.info(f"{j} = {lst[j]}")
					logging.warning('2\n')
					return res_lst
		res_lst[i] = res_i
	return res_lst


@profile
def func2(lst):
	len_lst = len(lst) - 1
	if len_lst == 0:
		logging.debug('one element')
		logging.info('wtf')
		logging.warning('1\n')
		return [0]
	
	first_lst = [0] * len_lst
	first_lst[0] = lst[0]
	for i in range(1, len_lst):
		first_lst[i] = first_lst[i - 1] * lst[i]
	
	lst = lst[::-1]
	
	second_lst = [0] * len_lst
	second_lst[0] = lst[0]
	for i in range(1, len_lst):
		second_lst[i] = second_lst[i - 1] * lst[i]
	second_lst = second_lst[::-1]

	res_lst = [0] * (len_lst + 1)
	res_lst[0] = second_lst[0]
	for i in range(len_lst - 1):
		res_lst[i + 1] = first_lst[i] * second_lst[i + 1]
	res_lst[len_lst] = first_lst[-1]

	return(res_lst)	



def main():
	func([1,2,3,4,5,6,7,8,9,10])
	func2([1,2,3,4,5,6,7,8,9,10])

	func([1,0,3,4,5,6,7,8,9,10])
	func2([1,0,3,4,5,6,7,8,9,10])

	func([1,2,3])
	func2([1,2,3])

	func([2,3,4,5,6])	
	func2([2,3,4,5,6])
	
	func([1])
	func2([1])

	func2(list(range(1,10000)))
	func(list(range(1,10000)))
	

if __name__ == "__main__":
	logging.basicConfig(filename = 'exemple.log', level = logging.DEBUG)
	main()
	p = pstats.Stats("func.txt")
	p.strip_dirs().sort_stats(-1).print_stats()
	p = pstats.Stats("func2.txt")
	p.strip_dirs().sort_stats(-1).print_stats()
