import sqlite3
from MyDescriptor import PositiveInt, StrUpper

CONNECT = sqlite3.connect("mydatabase.db")

class table(type):

	def __new__(cls, class_name, parents, attributes):
		return super().__new__(cls, class_name, parents, attributes)

	def __init__(self, class_name, parents, attributes):
		print("Create mydatabase.db")
		self.class_name = class_name
		try:
			cursor = CONNECT.cursor()
			cursor.execute(f"CREATE TABLE {class_name}\
							(id INTEGER PRIMARY KEY,\
							name TEXT NOT NULL)")
			print("Создаю таблицу")
			cursor.close()
		except :
			print("Таблица уже существует")
		super().__init__(class_name, parents, attributes)

	def __call__(self, *args, **kwargs):
		cursor = CONNECT.cursor()
		cursor.execute(f"INSERT INTO {self.class_name} VALUES {args}")
		CONNECT.commit()
		cursor.close()
		return super().__call__(*args, **kwargs)


class A(metaclass = table):

	id_name = PositiveInt()
	name = StrUpper()

	def __init__(self, id_name, name):
		self.start_id_name = id_name
		self.id_name = id_name
		self.name = name
	
	def save(self):
		cursor = CONNECT.cursor()
		cursor.execute(f"UPDATE A\
						SET id = {self.id_name}, name = '{self.name}'\
						WHERE id = {self.start_id_name}")
		CONNECT.commit()
		self.start_id_name = self.id_name
		cursor.close()

	@classmethod
	def all(cls):
		cursor = CONNECT.cursor()
		print("id\tname")
		for id_name, name in cursor.execute(f"SELECT * FROM {cls.class_name}"):
			print(f"{id_name}\t{name}")
			# добавить возвращение 
			# rfr django
		cursor.close()

	@classmethod
	def update(cls, **kwargs):
		cursor = CONNECT.cursor()
		lst = list(kwargs.items())
		sql = f"UPDATE {cls.class_name} SET {lst[0][0]} = "
		sql += f"{lst[0][1]} " if lst[0][0] == 'id' else f"'{lst[0][1]}' "
		sql += f"WHERE {lst[1][0]} = "
		sql += f"{lst[1][1]}" if lst[1][0] == 'id' else f"'{lst[1][1]}'"
		cursor.execute(sql)
		CONNECT.commit()
		cursor.close()
		return sql

	@classmethod
	def delete(cls, **kwargs):
		cursor = CONNECT.cursor()
		lst = list(kwargs.items())
		sql = f"DELETE FROM {cls.class_name} WHERE {lst[0][0]} = "
		sql += f"{lst[0][1]} " if lst[0][0] == 'id' else f"'{lst[0][1]}'"
		cursor.execute(sql)
		CONNECT.commit()
		cursor.close()
		return sql

	@classmethod
	def get(cls, **kwargs):
		cursor = CONNECT.cursor()
		lst = list(kwargs.items())
		sql = f"SELECT * FROM {cls.class_name} WHERE {lst[0][0]} = "
		sql += f"{lst[0][1]} " if lst[0][0] == 'id' else f"'{lst[0][1]}'"
		print("id\tname")
		for id_name, name in cursor.execute(sql):
			print(f"{id_name}\t{name}")
		cursor.close()
		return sql

#update
#save