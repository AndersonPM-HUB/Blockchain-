'''

Clase Opencloser
'''
import hashlib
import json


class Opencloser:

    def __init__(self):
        pass


    def hash(self, block):
        '''funcion de hash
        :param block: rebibe un bloque
        :returns hash
        '''
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash