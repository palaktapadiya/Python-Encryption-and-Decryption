import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_key_from_password(password: str, salt: bytes = None):
    """Derive a Fernet-compatible key from a password using PBKDF2 (SHA-256).
    Returns (key, salt). Keep the salt to re-derive the key for decryption."""
    if salt is None:
        salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt
