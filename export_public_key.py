import socket
from rsa_utility import load_private_key, load_public_key, export_public_key

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
            # Kirim kunci publik initiator
            conn.send(export_public_key(initiator_public_key))
        elif request == "GET_RESPONDER_KEY":
            # Kirim kunci publik responder
            conn.send(export_public_key(responder_public_key))
        else:
            print("Invalid request")

        conn.close()


if __name__ == "__main__":
    main()
