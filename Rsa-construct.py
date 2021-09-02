from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import construct
import binascii

exponent = input("enter exponent :")
modulus = input("enter modulus :")

e = int(exponent, 16) 
n = int(modulus, 16)  
pubkey = RSA.construct((n, e))
print(pubkey.exportKey())