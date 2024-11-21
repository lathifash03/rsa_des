#server.py
# python3 -m venv env
# source env/bin/activate
# pip install pycryptodome

# Buat private key untuk Server
# openssl genrsa -out server_private.pem 2048

# Buat public key untuk Server
# openssl rsa -in server_private.pem -outform PEM -pubout -out server_public.pem


import socket
from rsa_utility import load_private_key, load_public_key

# Load RSA keys
server_private_key = load_private_key("server_private.pem")
initiator_public_key = load_public_key("initiator_public.pem")
responder_public_key = load_public_key("responder_public.pem")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("Server (PKA) is running and waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection received from {addr}")

        # Receive request
        request = conn.recv(1024).decode()
        print(f"Request received: {request}")

        if request == "GET_INITIATOR_KEY":
            conn.send(initiator_public_key.export_key())
        elif request == "GET_RESPONDER_KEY":
            conn.send(responder_public_key.export_key())
        else:
            print("Invalid request")

        conn.close()


if __name__ == "__main__":
    main()
