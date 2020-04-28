import sqlite3
from MyDescriptor import PositiveInt, StrUpper


class table(type):

	def __new__(cls, class_name, parents, attributes):
		return super().__new__(cls, class_name, parents, attributes)

	def __init__(self, class_name, parents, attributes):
		print("Create mydatabase.db")
		self.class_name = class_name
		self.conn = sqlite3.connect("mydatabase.db")
		try:
			cursor = self.conn.cursor()
			cursor.execute(f"CREATE TABLE {class_name} (id integer, name text)")
			print("Создаю таблицу")
			cursor.close()
		except :
			print("Таблица уже существует")
		super().__init__(class_name, parents, attributes)

	def __call__(self, *args, **kwargs):
		cursor = self.conn.cursor()
		cursor.execute(f"INSERT INTO {self.class_name} VALUES {args}")
		self.conn.commit()
		cursor.close()
		return super().__call__(*args, **kwargs)


class A(metaclass = table):

	id_name = PositiveInt()
	name = StrUpper()

	def __init__(self, id_name, name):
		self.id_name = id_name
		self.name = name
	
	@classmethod
	def all(cls):
		cursor = cls.conn.cursor()
		print("id\tname")
		for id_name, name in cursor.execute(f"SELECT * FROM {cls.class_name}"):
			print(f"{id_name}\t{name}")
		cursor.close()

	@classmethod
	def update(cls, **kwargs):
		cursor = cls.conn.cursor()
		lst = list(kwargs.items())
		sql = f"UPDATE {cls.class_name} SET {lst[0][0]} = "
		sql += f"{lst[0][1]} " if lst[0][0] == 'id' else f"'{lst[0][1]}' "
		sql += f"WHERE {lst[1][0]} = "
		sql += f"{lst[1][1]}" if lst[1][0] == 'id' else f"'{lst[1][1]}'"
		cursor.execute(sql)
		cls.conn.commit()
		cursor.close()
		return sql

	@classmethod
	def delete(cls, **kwargs):
		cursor = cls.conn.cursor()
		lst = list(kwargs.items())
		sql = f"DELETE FROM {cls.class_name} WHERE {lst[0][0]} = "
		sql += f"{lst[0][1]} " if lst[0][0] == 'id' else f"'{lst[0][1]}'"
		cursor.execute(sql)
		cls.conn.commit()
		cursor.close()
		return sql

	@classmethod
	def get(cls, **kwargs):
		cursor = cls.conn.cursor()
		lst = list(kwargs.items())
		sql = f"SELECT * FROM {cls.class_name} WHERE {lst[0][0]} = "
		sql += f"{lst[0][1]} " if lst[0][0] == 'id' else f"'{lst[0][1]}'"
		print("id\tname")
		for id_name, name in cursor.execute(sql):
			print(f"{id_name}\t{name}")
		cursor.close()
		return sql