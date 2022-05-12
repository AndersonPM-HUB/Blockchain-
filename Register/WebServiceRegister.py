'''

WEB SERVICE DE REGISTER: http://127.0.0.1:5003

'''
import json

import requests
from flask import Flask, jsonify, make_response, request
app = Flask(__name__)

#---------------Peticion del cordinador ------------------------------------------------

@app.route('/registrar/<wallet>/<wallet_d>/<cantidad>', methods=['GET', 'POST'])
def Realizar_transaccion(wallet, wallet_d, cantidad):
    response = requests.get(url=f"http://172.19.0.2:5000/cuenta_existe/{wallet}/{wallet_d}")
    print(wallet)
    print(wallet_d)
    print(response.status_code)
    data = response.content
    data = data.decode()
    data = json.loads(data)
    print(data)


    if data == False:
        mensaje = 'No se encuentra alguna de las wallets'
    else :
        n = data['w1']
        c = int(n)
        print (n)

        cant =int(cantidad)
        print(cant)

        if cant > c:
            mensaje = 'No se puede hacer transaccion '

        else:
            mensaje = True
            response = requests.get(url=f"http://172.19.0.2:5000/registrar_en_Blockchain/{wallet}/{wallet_d}/{cant}")

        print(mensaje)

    return jsonify({'*': mensaje})



#--------------------Config Register --------------------------------------------------
if __name__ == '__main__':
    app.run(host='172.19.0.4', port=5003, debug=True)