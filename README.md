# RSA and DES Encryption System

This project demonstrates a secure communication system that integrates RSA encryption for key exchange and DES (Data Encryption Standard) encryption for data communication. It involves three main components:
1. **Server (Public Key Authority - PKA)**
2. **Initiator (Client A)**
3. **Responder (Client B)**

## Project Overview

The system follows a series of steps for secure communication:
1. **Key Exchange** using RSA encryption.
2. **Identity Verification** between Initiator A and the Server.
3. **Message Encryption** using RSA and data encryption using DES for actual communication.
4. **Communication Integrity** is ensured through encryption and decryption using the respective keys.

## Components

### 1. **Server (PKA)**
The server acts as a Public Key Authority (PKA). It is responsible for issuing the public keys of the Initiator and Responder and verifying the identity of the Initiator.

### 2. **Initiator (Client A)**
Initiator A requests public keys from the server, sends an encrypted message to Responder B using RSA encryption, and verifies the identity with the server. After the exchange of encrypted messages, the Initiator uses DES encryption to send data securely.

### 3. **Responder (Client B)**
Responder B decrypts the message from Initiator A, processes it, and sends an encrypted response back using RSA encryption.

### 4. **RSA and DES Implementation**
- **RSA** is used for securely exchanging keys and encrypting small pieces of data (e.g., symmetric encryption keys).
- **DES** is used for the encryption of actual data being transmitted.

## Requirements

- Python 3.x
- `pycryptodome` for DES encryption and RSA utilities
- `cryptography` for handling public/private key operations

To install dependencies:
```bash
pip install pycryptodome cryptography

How to Use

1. Generate RSA Keys
Before starting the system, you need to generate the RSA keys (private and public) for the server and clients.

For the server:

```
openssl genrsa -out server_private.pem 2048
openssl rsa -in server_private.pem -outform PEM -pubout -out server_public.pem

```

For the initiator and responder, repeat the steps to generate key pairs:

openssl genrsa -out initiator_private.pem 2048
openssl rsa -in initiator_private.pem -outform PEM -pubout -out initiator_public.pem

openssl genrsa -out responder_private.pem 2048
openssl rsa -in responder_private.pem -outform PEM -pubout -out responder_public.pem
2. Start the Server
To run the server (Public Key Authority - PKA), navigate to the directory containing the server.py script and run:

python server.py
3. Start the Initiator (Client A)
Once the server is running, you can start Initiator A by running:

python initiator_a.py
4. Start the Responder (Client B)
Finally, to start Responder B (waiting for encrypted messages from Initiator A), run:

python responder_b.py
Step-by-Step Process

Initiator A sends a request to the server for the public keys of both Initiator A and Responder B.
Server responds with the public keys of both clients.
Initiator A generates a unique ID and sends it to the server for verification.
Server verifies the ID and sends a confirmation back to Initiator A.
Initiator A encrypts a message using Responder B's public key (RSA) and sends it to Responder B.
Responder B receives the encrypted message, decrypts it using its private key, and processes the message.
Responder B encrypts a response using Initiator A's public key (RSA) and sends it back to Initiator A.
Initiator A decrypts the response using its private key.
For further communication, Initiator A and Responder B can now exchange data securely using DES encryption.
RSA Encryption and DES Encryption Flow

RSA Encryption: Used for encrypting small pieces of data (e.g., symmetric keys, messages) and for the secure exchange of keys between the clients and the server.
DES Encryption: After the RSA exchange, DES is used for the actual data encryption and decryption during the communication phase. The symmetric key generated from RSA is used to encrypt and decrypt the messages using DES.
RSA Encryption Example:
The initiator sends an encrypted message using Responder B's public RSA key. The responder decrypts the message with its private RSA key. Similarly, the server can also encrypt/decrypt the identity verification messages using RSA.

DES Encryption Example:
Once the public keys are exchanged, DES is used to encrypt larger pieces of data, such as file content or longer messages. The key for DES is securely exchanged using RSA, and the actual communication uses DES for faster encryption and decryption of larger data.

Code Structure

The project is structured as follows:

rsa_des_encryption_system/
├── initiator_a.py            # Initiator A's code for handling communication and encryption
├── responder_b.py            # Responder B's code for receiving and decrypting messages
├── server.py                 # Server code (PKA) for providing public keys and verifying identity
├── rsa_utility.py            # Utility functions for loading and saving keys, RSA and DES operations
├── initiator_private.pem     # Private key of Initiator A
├── initiator_public.pem      # Public key of Initiator A
├── responder_private.pem     # Private key of Responder B
├── responder_public.pem      # Public key of Responder B
├── server_private.pem        # Private key of Server (PKA)
├── server_public.pem         # Public key of Server (PKA)
└── README.md                 # Project Documentation (this file)
Security Considerations

RSA is secure for key exchange and small data encryption but is slow for large data sets. For actual data transmission, DES (or AES) is preferred.
DES is an older encryption algorithm. While it is used here for demonstration, it is not considered secure for modern cryptographic purposes. For production environments, AES (Advanced Encryption Standard) should be used instead.
Future Enhancements

Implement AES instead of DES for stronger encryption.
Introduce authentication mechanisms to ensure the integrity and authenticity of messages.
Add support for digital signatures to verify the sender of messages.
Improve key management and revocation mechanisms.
License

This project is open source and available under the MIT License.
