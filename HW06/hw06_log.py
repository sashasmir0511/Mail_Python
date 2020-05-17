import logging


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


def main():
	func([1,2,3,4,5,6,7,8,9,10])
	func([1,0,3,4,5,6,7,8,9,10])
	func([1,2,3])
	func([1])
	func([1,2,3,'a',[10,20]])

if __name__ == "__main__":
	logging.basicConfig(filename = 'exemple.log', level = logging.DEBUG)
	main()