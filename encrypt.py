
from pyDes import des, CBC, PAD_PKCS5
import binascii
 
# Clave secreta
KEY='mHAxsLYz'
def des_encrypt(s):
    """
         Cifrado DES
         : param s: cadena sin procesar
         : return: cadena encriptada, hexadecimal
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)
 
 
def des_descrypt(s):
    """
         Descifrado DES
         : param s: cadena encriptada, hexadecimal
         : return: cadena descifrada
    """
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de

s= 'Holafeos'
print(s)
print(des_encrypt(s))
print(des_descrypt(s))