import logging

def func(lst):
	len_lst = len(lst)
	if len_lst == 1:
		logging.debug('one element')
		logging.info('wtf')
		#logging.warning('[0]')
		return [0]
	res_lst = [0] * len_lst
	for i in range(len_lst):
		res_i = 1
		for j in range(i):
			res_i *= lst[j]
		for j in range(i + 1, len_lst):
			res_i *= lst[j]
		res_lst[i] = res_i
	logging.debug('more element')
	logging.info('wtf')
	#logging.warning(str(res_lst))
	return res_lst


def main():
	func([1,2,3,4,5,6,7,8,9,10])
	func([1,0,3,4,5,6,7,8,9,10])
	func([1,2,3])
	func([1])

if __name__ == "__main__":
	logging.basicConfig(filename = 'example.log', level = logging.DEBUG)
	main()