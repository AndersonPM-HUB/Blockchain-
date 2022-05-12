import hashlib

from Blockchain import Blockchain

# se cre objeto blockchain
b = Blockchain()
# se generan cuantas
n =b.generar_cuenta('juan', 1000)
x =b.generar_cuenta('maria', 1000)
# se listan usuarios
print(f'lista de usuarios {b.usuarios}')
# se listan trnasaccuines
print(len(b.current_transactions))
# se generan transacciones
b.new_transaction(n, x, 2000)
b.new_transaction(n, x, 2000)
b.new_transaction(n, x, 2000)
print('total transacciones', len(b.current_transactions))
print(len(b.current_transactions))
m = hashlib.sha256(b"mensaje").hexdigest()
b.new_block(m)
b.hash(m)
m = hashlib.sha256(b"m").hexdigest()
b.new_block(m)
b.hash(m)
m = hashlib.sha256(b"mw").hexdigest()
b.new_block(m)
b.hash(m)
print('blockchain'.center(100,'*'))

for n in b.blockchain:
    print(n)
