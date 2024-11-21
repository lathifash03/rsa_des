#initiator_a.py

import socket
from rsa_utility import load_public_key, load_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def send_encrypted_message():
    """
    Fungsi untuk mengirim pesan terenkripsi ke responder.
    """
    # Muat kunci publik responder dari file
    responder_public_key = load_public_key("responder_public.pem")

    # Muat kunci privat initiator
    initiator_private_key = load_private_key("initiator_private.pem")

    # Ambil input pesan dari pengguna
    message = input("Masukkan pesan yang ingin dikirim: ")

    # Enkripsi pesan menggunakan kunci publik responder
    encrypted_message = responder_public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Kirim pesan terenkripsi ke server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 3006))
    client_socket.send(encrypted_message)
    print("Pesan terenkripsi dikirim:", encrypted_message)

    # Terima respons terenkripsi dari server
    encrypted_response = client_socket.recv(1024)
    decrypted_response = initiator_private_key.decrypt(
        encrypted_response,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Pesan setelah dekripsi: {decrypted_response.decode()}")
    client_socket.close()

if __name__ == '__main__':
    send_encrypted_message()
