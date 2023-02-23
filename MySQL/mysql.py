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
		results = conn.execute(query)
		conn.close()
		return results

	def query(self, query):
		return self.__exec_query(query)
