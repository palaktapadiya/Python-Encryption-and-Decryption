Problem Statement
With increasing digital communication, sensitive information such as documents, messages, and files must be protected from unauthorized access. There is a need for a simple and secure tool that can encrypt and decrypt data using a password-based system.  
This project solves the problem of protecting text and files by using strong cryptographic techniques.

Scope of the Project
The project covers the following:
- Secure key generation using PBKDF2-HMAC  
- Text encryption and decryption  
- File encryption and decryption for multiple formats  
- Logging of all actions for auditing  
- Error handling and validation  
- Menu-driven terminal interface  
- Modular program structure with separate Python files  

The project does *not* include GUI, networking features, or cloud storage (but can be added in future enhancements).

Target Users
This tool is intended for:
- Students learning cryptography  
- Users who want to protect personal files  
- Beginners learning file handling in Python  
- Anyone who needs a simple offline encryption tool  
- Educational and academic demonstrations  

High-Level Features
- Password-based key generation  
- Symmetric encryption using Fernet  
- Text encryption/decryption support  
- File encryption/decryption support (PDF, images, documents)  
- Automatic logging to logs.json  
- Modular design (main, encryption, decryptor, key_manager, file_ops, audit_log)  
- Error handling for wrong file paths & incorrect passwords  
- Clean and easy-to-use CLI menu
