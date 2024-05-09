from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

import base64

from ..models import Cliente

def encrypt_message(private_key, message):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher.encrypt(message.encode())
    # Codificar el mensaje cifrado en Base64 para obtener una cadena de texto
    encrypted_message_base64 = base64.b64encode(encrypted_message).decode()
    return encrypted_message_base64

def decrypt_message(public_key, encrypted_message_base64):
    # Decodificar el mensaje cifrado desde Base64
    encrypted_message = base64.b64decode(encrypted_message_base64.encode())
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

def generate_key_pair():
    key_pair = RSA.generate(2048)
    private_key = key_pair.export_key()
    public_key = key_pair.publickey().export_key()
    return public_key, private_key

def calculate_hash(message):
    hash_object = hashlib.sha256(message.encode())
    return hash_object.hexdigest()

def get_clientes():
    queryset = Cliente.objects.all()
    return (queryset)