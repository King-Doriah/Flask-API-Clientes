import pymysql

class DBConnection:
	def __init__(self, db_data):
		try:
			self.connection = pymysql.connect(host=db_data['HOSTNAME'], user=db_data['USERNAME'], passwd=db_data['PASSWORD'], db=db_data['DATABASE'])
			self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
		except Exception as error:
			return error

	def selectClientes(self):
		try:
			stmt = "SELECT * FROM clientes ORDER BY id"
			self.cursor.execute(stmt)
			return self.cursor.fetchall()
		except Exception as error:
			return error

	def selectCliente(self, id):
		try:
			stmt = f"SELECT * FROM clientes WHERE id = {id} ORDER BY id"
			self.cursor.execute(stmt)
			return self.cursor.fetchone()
		except Exception as error:
			return error
