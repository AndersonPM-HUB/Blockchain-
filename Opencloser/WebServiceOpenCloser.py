'''
WEB SERVICE OPENCLOSER : http://127.0.0.1:5004
'''

from flask import Flask, jsonify
from OpenCloser import Opencloser

app = Flask(__name__)

o = Opencloser()
@app.route('/generar_hash/<bloque>', methods=['POST','GET'])
def generar_hash(bloque):
    # print(bloque)
    hash= o.hash(bloque)
    print(''.center(100,'-'))
    print(f'{ hash  }')

    return jsonify({'hash':hash})



#---------------Config del componente------------------------------------------

if __name__ == '__main__':
    app.run(host='172.19.0.5', port=5004, debug=True)

