from cryptography.fernet import Fernet
from file_ops import read_file_bytes, write_file_bytes

def decrypt_text(token, key):
    f = Fernet(key)
    return f.decrypt(token).decode()

def decrypt_file(path, key):
    f = Fernet(key)
    data = read_file_bytes(path)
    decrypted = f.decrypt(data)
    out = path.replace(".enc", ".dec")
    write_file_bytes(out, decrypted)
    return out
