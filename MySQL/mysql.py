import mysql.connector


class MySQL:

	__config = {
		'user': 'root',
		'password': 'catalinROOT',
		'host': 'localhost',
		'database': 'read_all'
	}
	__instance = None

	def __new__(cls):
		if cls.__instance is None:
			cls.__instance = super().__new__(cls)
		return cls.__instance

	def __exec_query(self, query):
		conn = mysql.connector.connect(**self.__config)
		cursor = conn.cursor()
		cursor.execute(query)
		column_names = [i[0] for i in cursor.description]

		results = cursor.fetchall()

		rows = []
		for row in results:
			row_dict = {}
			for i, column_name in enumerate(column_names):
				row_dict[column_name] = row[i]
			rows.append(row_dict)

		conn.close()
		return rows

	def query(self, query):
		return self.__exec_query(query)
