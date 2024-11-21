# rsa_utility

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def load_public_key(file_path):
    """
    Fungsi untuk memuat kunci publik dari file PEM.
    """
    try:
        with open(file_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())
        return public_key
    except Exception as e:
        raise ValueError(f"Error loading public key: {e}")


def load_private_key(file_path):
    """
    Fungsi untuk memuat kunci privat dari file PEM.
    """
    try:
        with open(file_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())
        return private_key
    except Exception as e:
        raise ValueError(f"Error loading private key: {e}")


def export_public_key(key):
    """
    Fungsi untuk mengekspor kunci publik ke format PEM.
    """
    pem = key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return pem


def export_private_key(key):
    """
    Fungsi untuk mengekspor kunci privat ke format PEM.
    """
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem
