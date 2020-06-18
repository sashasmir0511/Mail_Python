import os
import sys
import datetime
import xlwt


def get_data(path, data, level=0):
	name = path
	size = f"{os.path.getsize(path)} B"
	date_changes = datetime.datetime.fromtimestamp(os.path.getmtime(path)).isoformat()
	abs_path = os.path.abspath(path)
	if os.path.isfile(path):
		data.append([name, "file", size, date_changes, abs_path, level])
	if os.path.isdir(path):
		data.append([name, "dir", size, date_changes, abs_path, level])
		for file in os.listdir(path):
			path_file = f"{path}/{file}"
			get_data(path_file, data, level+1)


if __name__ == "__main__":
	path = sys.argv[1]
	data = [["Имя", "Тип", "Размер", "Дата", "Абсолютный путь", "Уровень вложенности"]]
	get_data(path, data)
	book = xlwt.Workbook()
	sheet1 = book.add_sheet("Sheet1")
	for num in range(len(data)):
		row = sheet1.row(num)
		for col in range(len(data[num])):
			value = data[num][col]
			row.write(col, value)
	book.save("tqwer.xls")
