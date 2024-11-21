from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import DES


def des_encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text.encode(), DES.block_size)
    encrypted_text = des.encrypt(padded_text)
    encrypted_binary = ''.join(format(byte, '08b') for byte in encrypted_text)
    return encrypted_binary


def des_decrypt(encrypted_binary, key):
    encrypted_bytes = int(encrypted_binary, 2).to_bytes(len(encrypted_binary) // 8, byteorder='big')
    des = DES.new(key, DES.MODE_ECB)
    decrypted_padded_text = des.decrypt(encrypted_bytes)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    return decrypted_text.decode()
