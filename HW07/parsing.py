import requests
import re
from bs4 import BeautifulSoup
from operator import itemgetter
from http_R import JsonResponse
from collections import Counter

def func_parsing(request):
	web_page = requests.get(request).text
	web_page_soup = BeautifulSoup(web_page, features='html.parser')
	web_page_text = web_page_soup.get_text()
	web_page_words = [word.lower() for word in re.split(r'\W', web_page_text)]
	words_counter = Counter()
	for word in web_page_words:
			words_counter[word] += 1
	words_counter = dict(sorted(words_counter.items(), key=itemgetter(1), reverse=True)[1:11])
	# print(words_counter)
	return JsonResponse(data=words_counter)

if __name__ == '__main__':
	print(func_parsing("https://pythonworld.ru/moduli/modul-collections.html").data)
