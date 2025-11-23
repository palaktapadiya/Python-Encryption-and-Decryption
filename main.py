import os
from key_manager import generate_key_from_password
from encryptor import encrypt_text, encrypt_file
from decryptor import decrypt_text, decrypt_file
from audit_log import log

def main():
    print("🔐 EASY ENCRYPTION TOOL (Gold-Level)")
    password = input("Enter password for encryption/decryption: ")
    key, salt = generate_key_from_password(password)
    print("(Tip: Keep your password safe. Salt is kept in memory for this run.)")

    while True:
        print("\n1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Encrypt File")
        print("4. Decrypt File")
        print("5. Show logs.json path")
        print("6. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            text = input("Enter text: ")
            encrypted = encrypt_text(text, key)
            print("\nEncrypted token (copy & save):\n", encrypted.decode())
            log("encrypt_text")
        elif choice == "2":
            token = input("Enter encrypted token: ").encode()
            try:
                decrypted = decrypt_text(token, key)
                print("\nDecrypted text:\n", decrypted)
                log("decrypt_text")
            except Exception as e:
                print("Decryption failed:", e)
                log("decrypt_text", status="FAILED", extra={"error": str(e)})
        elif choice == "3":
            path = input("File path to encrypt: ").strip()
            if not os.path.exists(path):
                print("File not found.")
                continue
            out = encrypt_file(path, key)
            print("Encrypted file saved as:", out)
            log("encrypt_file", filename=path)
        elif choice == "4":
            path = input("Encrypted file path (.enc): ").strip()
            if not os.path.exists(path):
                print("File not found.")
                continue
            try:
                out = decrypt_file(path, key)
                print("Decrypted file saved as:", out)
                log("decrypt_file", filename=path)
            except Exception as e:
                print("Decryption failed:", e)
                log("decrypt_file", status="FAILED", extra={"error": str(e)})
        elif choice == "5":
            print(os.path.join(os.path.dirname(__file__), "..", "logs.json"))
        else:
            break

if __name__ == "__main__":
    main()
