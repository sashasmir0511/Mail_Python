# not n^2
# todo n
def func(lst):
	len_lst = len(lst)
	if len_lst == 1:
		return [0]
	res_lst = [0] * len_lst
	for i in range(len_lst):
		res_i = 1
		for j in range(len_lst):
			if j != i:
				if isinstance(lst[j], int):
					res_i *= lst[j]
				else:
					return res_lst
		res_lst[i] = res_i
	return res_lst


def main():
	# random 
	func([1,2,3,4,5,6,7,8,9,10])
	func([1,0,3,4,5,6,7,8,9,10])
	func([1,2,3])
	func([1])
	func([1,2,3,'a',[10,20]])

if __name__ == "__main__":
	main()