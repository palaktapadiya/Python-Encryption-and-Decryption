from cryptography.fernet import Fernet
from file_ops import read_file_bytes, write_file_bytes

def encrypt_text(text, key):
    f = Fernet(key)
    return f.encrypt(text.encode())

def encrypt_file(path, key):
    f = Fernet(key)
    data = read_file_bytes(path)
    encrypted = f.encrypt(data)
    out = path + ".enc"
    write_file_bytes(out, encrypted)
    return out
