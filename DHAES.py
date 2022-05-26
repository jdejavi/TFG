#!/usr/bin/python3
'''
Implementacion del algoritmo de ECDH y cifrador con el algoritmo AES modo EAX
    Autor --> Javier Matilla Martin maatii@usal.es (maatii at usal)
    Se hace uso de las funciones del script de uso publico de Andrea Corbellini:
        - https://github.com/andreacorbellini/ecc/blob/master/scripts/ecdsa.py
'''

import ecdsa
import random
import hashlib
from Crypto.Cipher import AES
import base64
import pyperclip as clipboard

# Son las funciones para encriptar y desencriptar con el AES-EAX
#   - Encriptar, pasa a bytes el mensaje, obtiene el IV a partir del modo de operacion y la clave,
#     luego cifra y obtiene el texto cifrado y el MAC (Codigo de autenticacion de mensajes) calculado durante el cifrado.
#   - Desencriptar saca cada valor por separado, IV, MAC y el texto cifrado de lo que te envian, crea una nueva instancia de 
#     AES-EAX y devuelve el texto desencriptado y verificado

#str(desencriptarAES_EAX(secretoBobT.encode(),msgPaBob)).replace("b'","").replace("'","")
#encriptarAES_EAX(secretoAliceT.encode(),message)

def encriptarAES_EAX(clave, mensaje):
    bytes = mensaje.encode()
    cifrado = AES.new(clave,AES.MODE_EAX)
    ciphertext,mac = cifrado.encrypt_and_digest(bytes)
    return cifrado.nonce + mac + ciphertext

def desencriptarAES_EAX(clave, mensaje):
    iv = mensaje[:AES.block_size]
    
    mac = mensaje[AES.block_size:AES.block_size*2]
    
    cifradoTexto = mensaje[AES.block_size*2:]
    
    cifrado = AES.new(clave, AES.MODE_EAX,iv)
    return cifrado.decrypt_and_verify(cifradoTexto,mac)

def ECDH_secretTrunc(private,public):
    #Aqui se hace el diffie-helmann para obtener el punto, como solo nos interesa la x, nos quedamos con ella
    point = ecdsa.scalar_mult(private,public)
    return str(point[0])[:32]