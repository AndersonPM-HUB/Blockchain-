'''

WEB SERVICE DE BLOCKCHAIN : http://127.0.0.1:5002

'''
import json

import requests
from flask import Flask, jsonify
from Blockchain import Blockchain


app = Flask(__name__)
b = Blockchain()
# --------------------------------------Servicios para wallet----------------------------
@app.route('/users')
def mostrar_usuarios():

    usuarios =''
    for n , v in b.usuarios.items():
        usuarios += f'[{n} = {v}] | '
    return usuarios


@app.route('/generar_wallet/<nombre>/<dinero>', methods=['GET', 'POST'])
def crear_wallet(nombre,dinero):
    print(nombre)
    w = b.generar_cuenta(nombre, dinero)
    return jsonify({'Tu direccion de wallet es':w, 'dinero':dinero})


@app.route('/consultar/<nombre>', methods=['POST','GET'])
def consulta_wallet(nombre):
    # for usuario , valor in b.usuarios.items():
    if nombre in b.usuarios:
            r = b.usuarios[nombre]
            print(r)
    else :
            r = 'no se encuentra usuario'

    return jsonify({'RTA ':r})

#------------------------------Servicio para register -----------------------------------------

@app.route('/consultar_existencia/<wallet>/<wallet_d>' , methods=['POST','GET'])
def cuenta_existe(wallet, wallet_d):
    print(wallet)
    print(b.usuarios)
    if wallet in b.usuarios and wallet_d in b.usuarios:
         mensaje ={
               'w1' : b.usuarios[wallet],
               'w2':b.usuarios[wallet_d],
            }
    else :
        mensaje = False

    print(mensaje)

    return mensaje


@app.route('/registrar_blockchain_t/<w1>/<w2>/<cant>', methods=['GET', 'POST'])
def registrar_transaccion(w1, w2, cant):
    cantidad = int(cant)
    t = b.new_transaction(w1,w2,cantidad)
    print(b.current_transactions)
    b.restar_valor(w1,cantidad)
    b.sumar_valor(w2,cantidad)
    print(len(b.current_transactions))
    if len(b.current_transactions) % 3==0:
        response = requests.get(url=f"http://172.19.0.2:5000/cerrar_bloque/{b.last_block}")
        data= response.content
        data =data.decode()
        data = json.loads(data)
        print(data)
        b.new_block(data)
        b.hash(data['hash'])
    return jsonify(t)



@app.route('/ver_blockchain', methods=['GET','POST'])
def ver_blockchain():

    return jsonify({'blockchain': b.blockchain})



#--------------------Config cordinador --------------------------------------------------
if __name__ == '__main__':
    app.run(host='172.19.0.3', port=5002, debug=True)

