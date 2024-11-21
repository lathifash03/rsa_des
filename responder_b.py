# responder_b.py

import socket
from rsa_utility import load_public_key, load_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def receive_encrypted_message():
    """
    Fungsi untuk menerima dan mendekripsi pesan dari initiator.
    """
    # Muat kunci publik responder dari file
    responder_public_key = load_public_key("responder_public.pem")

    # Muat kunci privat responder
    responder_private_key = load_private_key("responder_private.pem")

    # Setup server untuk menerima koneksi
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 3006))
    server_socket.listen(1)
    print("Server berjalan dan menunggu koneksi dari client...")

    conn, addr = server_socket.accept()
    print(f"Koneksi diterima dari {addr}")

    # Terima pesan terenkripsi
    encrypted_message = conn.recv(1024)

    # Dekripsi pesan menggunakan kunci privat responder
    decrypted_message = responder_private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Pesan setelah dekripsi: {decrypted_message.decode()}")

    # Kirim respons terenkripsi kembali ke initiator
    response_message = input("Masukkan respons untuk dikirim: ")
    encrypted_response = responder_public_key.encrypt(
        response_message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    conn.send(encrypted_response)
    print(f"Pesan terenkripsi dikirim ke initiator: {encrypted_response}")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    receive_encrypted_message()
