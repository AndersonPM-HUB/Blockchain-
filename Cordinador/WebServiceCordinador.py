'''
Web service de Cordinador : http://127.0.0.1:5000
'''

import requests
from flask import Flask, render_template, request, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

#----------------Metodo de error--------------------------------------------------------------
@app.errorhandler(404)
def manejo_error(error):
    return render_template('404.html')

#-----------------Metodos para renderear a las diferrentes vistas------------------------------
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/generar')
def generar_wallet():
    return render_template('Generar.html')

@app.route('/registrar')
def registrar():
    return render_template('Registrar.html')

@app.route('/consultar')
def consultar():
    return render_template('Consultar.html')

@app.route('/ver')
def ver_blockchain():
    response = requests.get(url=f"http://172.19.0.3:5002/ver_blockchain")
    data = response.content
    data = data.decode()
    data = json.loads(data)
    return render_template('Blockchain.html', data = data)

@app.route('/ver_usuarios')
def ver_usuarios():
    response = requests.get(url=f"http://172.19.0.3:5002/users")
    data = response.content
    data = data.decode()
    data = json.dumps(data)
    return render_template('usuarios.html', data=data)

# ------------------------------------Servicios Wallet-------------------------------------------------------
@app.route('/crear_cuenta', methods=['GET', 'POST'])
def crear_cuenta():
    nombre = request.form['user']
    dinero = request.form['dinero']
    monto = int(dinero)
    print(nombre)
    response = requests.get(url=f"http://172.19.0.3:5002/generar_wallet/{nombre}/{monto}")
    data = response.content
    data = data.decode()
    data = json.loads(data)
    return render_template('Generar.html', data = data)

#----------------------registrar transaccion ----------------------------------------------------
@app.route('/registrar_transaccion', methods=['GET', 'POST'])
def registrar_transaccion():

    wallet = request.form['user']
    wallet_d = request.form['user_des']
    cantidad = request.form['monto']
    monto = int(cantidad)
    print(f'{wallet}{wallet_d}{monto}')
    response = requests.get(url=f"http://172.19.0.4:5003/registrar/{wallet}/{wallet_d}/{monto}")
    data = response.content
    data = data.decode()
    data = json.loads(data)
    return render_template('Registrar.html', data=data)
# ----------------------------Consultar fondo ----------------------------------------

@app.route('/consultar_fondo', methods=['GET', 'POST'])
def consultar_fondo():
    wallet = request.form['user_name']
    response = requests.get(url=f"http://172.19.0.3:5002/consultar/{wallet}")
    data = response.content
    data = data.decode()
    data = json.loads(data)
    return render_template('Consultar.html', data=data)

# ------------------------------------WebServicio Register-------------------------------------------------------

@app.route('/cuenta_existe/<wallet>/<wallet_d>' , methods=['POST','GET'])
def cuenta_existe_c(wallet, wallet_d):
    response = requests.get(url=f"http://172.19.0.3:5002/consultar_existencia/{wallet}/{wallet_d}")
    data = response.content
    data = data.decode()
    data = json.loads(data)
    return data

#------------------------------------Metodo para registrar transaccion en blockchain ------------------------------

@app.route('/registrar_en_Blockchain/<wallet>/<wallet_d>/<cantidad>',methods=['POST', 'GET'])
def registrar_transferencia(wallet, wallet_d, cantidad ):
    response = requests.get(url=f"http://172.19.0.3:5002/registrar_blockchain_t/{wallet}/{wallet_d}/{cantidad}")
    print(f' esta es la wallet {wallet}')
    return response.content

#------------------------------------WEB SERVISE OPENCLOSER-----------------------------------------
@app.route('/cerrar_bloque/<bloque>' ,methods=['POST', 'GET'])
def cerrar_bloque(bloque):
    response = requests.get(url=f"http://172.19.0.5:5004/generar_hash/{bloque}")
    print(response)
    data = response.content
    data =data.decode()
    data = json.loads(data)
    print(f' bloque {bloque}')
    print(type(data))
    return data


#--------------------------Config cliente -----------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
