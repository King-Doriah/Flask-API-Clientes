from flask import Flask, request, jsonify
from dbconnection import DBConnection

db_data = {}

db_data['HOSTNAME'] = '127.0.0.1'
db_data['USERNAME'] = 'miraldino'
db_data['PASSWORD'] = 'paulo302'
db_data['DATABASE'] = 'api_1'

db = DBConnection(db_data)

app = Flask(__name__)

@app.route('/')
def home():
	web = '''
<h1><center>A API está funcionando...</center></h1><br>

/clientes	==> Exibir todos os clientes.<br>
/cliente/<id>	==> Exibir apenas um cliente pelo seu ID.
	'''
	return web

@app.route('/clientes')
def clientes():
	rows = db.selectClientes()
	if rows:
		return jsonify(rows)
	else:
		msg = {'msg': 'Nenhum cliente encontrado no sistema.'}
		return jsonify(msg)

@app.route('/cliente/<int:id>')
def cliente(id):
	row = db.selectCliente(id)
	if row:
		return jsonify(row)
	else:
		msg = {'msg': 'Cliente não encontrado.'}
		return jsonify(msg)

if __name__ == '__main__':
	app.run(debug=True)
