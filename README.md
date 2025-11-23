# Python-Encryption-and-Decryption
A simple, secure, and modular Python-based system for encrypting and decrypting text and files using the cryptography library. This project demonstrates real-world cryptographic concepts such as password-based key derivation, symmetric encryption, and file handling in Python.

Overview of the Project

This project allows users to securely encrypt and decrypt:
- Plain text  
- Any file type (PDF, TXT, images, etc.)  
The system uses *Fernet symmetric encryption* along with *PBKDF2-HMAC (SHA256)* to derive a cryptographic key from the user's password. Every action (encrypt/decrypt) is recorded in a log file (logs.json), making the tool suitable for academic learning and secure data handling.
The project follows a modular structure ensuring clarity, maintainability, and scalability.


Features

- Text Encryption
- Text Decryption
- File Encryption (PDF, PNG, TXT, DOCX, etc.)
- File Decryption
- Password-based key generation
- Automatic logging (logs.json)
- Error handling for wrong paths, invalid tokens, incorrect passwords
- Modular structure with multiple Python files


Technologies / Tools Used
- Python 3
- cryptography library
  - Fernet
  - PBKDF2HMAC (SHA-256)
- JSON for logging
- OS module
- Time module
- VS Code / Terminal / CMD


Steps to Install & Run the Project

▶ 1. Clone this repository

▶ 2. Install required dependencies
pip install cryptography

▶ 3. Navigate to the project folder
cd EncryptDecrypt

▶ 4. Run the program
python main.py


Instructions for Testing

✔ 1. Test Text Encryption
Select Option 1
Enter a sample message
Confirm that the encrypted token is generated
Check logs.json entry

✔ 2. Test Text Decryption
Copy ciphertext from previous step
Select Option 2
Verify correct plaintext is returned

✔ 3. Test File Encryption
Place a file inside the project folder (e.g., sample.pdf)
Select Option 3
Enter file name
Look for output file: sample.pdf.enc

✔ 4. Test File Decryption
Select Option 4
Enter the encrypted file name (e.g., sample.pdf.enc)
Confirm restored file is generated

✔ 5. Check Logs
Open logs.json to verify detailed history of operations.
