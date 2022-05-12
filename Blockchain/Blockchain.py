import hashlib
import json
import random

from flask import jsonify

class Blockchain(object):
    '''Clase blockchain '''

    hash_genesis = hashlib.sha224(b"genesis").hexdigest()
    preview_hash= [hash_genesis]
    def __init__(self):
        '''contructor de la clase '''
        self.blockchain = [] #lista de bloques
        self.current_transactions = [] # lista de trnasacciones en un bloque
        self.usuarios ={} #lista usuarios
        # Crea el bloque génesis
        self.new_block(hash=self.hash_genesis, previous_hash='0'*64)


    def new_block(self,hash, previous_hash=None):
        """
        Crear un nuevo Bloque en el Cadena de Bloques
        :param previous_hash: (Opcional) <str> Hash del Bloque anterior
        :return: <dict> Nuevo Bloque
        """
        block = {
            'index': len(self.blockchain) + 1,
            'nonce': random.randint(100, 200),
            'transactions': self.current_transactions,
            'previous_hash': self.preview_hash[len(self.preview_hash)-1]or previous_hash,
            'hash':hash,
        }

        # Anular la lista actual de transacciones
        self.current_transactions = []
        self.blockchain.append(block)

        return block

    @property
    def last_block(self):
        '''Para que podamos llamar a nuestra cadena y recibir el bloque que se agregó más recientemente '''
        return self.blockchain[-1]


    def new_transaction(self, sender, recipient, amount):
        """
        Crea una nueva transacción para ir al siguiente Bloque minado
        :param sender: <str> Dirección del remitente
        :param recipient: <str> Dirección del destinatario
        :param amount: <int> Cantidad
        :return: <int> El índice del Bloque que llevará a cabo esta transacción
        """
        transaccion = {
            'envia': sender,
            'recibe': recipient,
            'cantidad': amount,
        }

        self.current_transactions.append(transaccion)
        return self.current_transactions

    def hash(self,hash):
        """
              funcion para recibir hash
              :param hash:
              :returns: <hash> hash
              """
        Blockchain.preview_hash.append(hash)
        return hash



#-----------------------------------------------------------------------------
    def generar_cuenta(self,nombre, dinero):
        '''funcion que genera y agrega una nueva direccion de wallet al sistema
        :param nombre:<string> nombre que digita el usuario
        :returns: <string >clave


        '''
        dir = random.randint(100 ,300)
        dire = str(dir)
        d= int(dinero)
        clave =(nombre+dire)
        self.usuarios.update({clave : d})
        print(self.usuarios)
        return clave
#--------------------------------------------------------------------------------
    def cuenta_existe(self, cuenta):
        '''funcion que retorna si la cuenta existe '''
        for u in self.usuarios.keys():
            if cuenta == u:
                return True
        return False
#--------------------------------------------------------------------------------

    def __str__(self):
        '''
        imprime el contenido de la blockchain
        '''

        lista_bloques = []
        for block in self.blockchain:
            lista_bloques.append(block)


        return {'blockchain': lista_bloques}

#---------------------------------------------------------------------------------

    def restar_valor(self, wallet , cantidad):
        '''funcion que resta el valor de la wallet que envia '''
        c = int(cantidad)
        for u in self.usuarios:
            if wallet == u:
                v=int(self.usuarios[wallet])
                rta = v-c
                self.usuarios[wallet]=rta
                print(f'{v} -{c} ={rta}')
                return rta

    def sumar_valor(self, wallet , cantidad):
        '''funcion que suma el valor que envia la wallet 1 a wallet 2'''
        c = int(cantidad)
        for u in self.usuarios:
            if wallet == u:
                v=int(self.usuarios[wallet])
                rta = v+c
                self.usuarios[wallet] = rta
                print(f'{v} + {c} = {rta}')
                return rta

#-----------------------------------------------------------------------------

