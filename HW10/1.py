import re
import sys


def get_count_pages_pdf(filename):
	count = 0
	re_pattern = re.compile("Page\W")
	with open(filename, "rb") as f:
		for line in f:
			if re_pattern.search(str(line)) and "Pages" not in str(line):
				# print(line)
				count += 1
	return count


if __name__ == "__main__":
	filename = sys.argv[1]
	count_pages = get_count_pages_pdf(filename)
	print(count_pages)
