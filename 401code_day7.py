#!/usr/bin/env python3

# Developed after watching class review for assistance

# Add a feature capability to your script to:

# Recursively encrypt a single folder and all its contents.

# Recursively decrypt a single folder that was encrypted by this tool.

# Import libraries
import os
from cryptography.fernet import Fernet

# Define functions
# Key generation
def generate_key():
    return Fernet.generate_key()

# Load Key and return as bytes
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()
    
# Save the Key into a file
def save_key(key_file, key):
    with open(key_file, 'wb') as file:
        file.write(key)

# Encrypt file with fernet key
def encrypt_file(key, input_file, output_file):
    fernet = Fernet(key)

# Read input content & encrypt
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)

# Write encrypted data into output file
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Decryt data with fernet key
def decrypt_file(key, input_file, output_file):
    fernet = Fernet(key)

# Read input conent and decrypt
    with open(input_file, 'rb') as file:
        data = file.read()
    decrypted_data = fernet.decrypt(data)

# Writes decrypt data into output file
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# Convert message into bytes, encrypt with fernet key
def encrypt_message(key, message):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())

#print encrypted message as a string
    print("Encrypted message:", encrypted_message.decode())

# Fernet key and encrypted message 
def decrypt_message(key, encrypted_message):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())

#print decrypted message as a string
    print("Decrypted message:", decrypted_message.decode())

# Recursive folder and contents and key to encrypt
def encrypt_folder(key, input_folder, output_folder):
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            input_file = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(input_file, input_folder)
            output_file = os.path.join(output_folder, relative_path)
            encrypt_file(key, input_file, output_file)

# Recursive folder and contents and key to decrypt
def decrypt_folder(key, input_folder, output_folder):
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            input_file = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(input_file, input_folder)
            output_file = os.path.join(output_folder, relative_path)
            decrypt_file(key, input_file, output_file)

# Main
# Check if encryption key exists
def main():
    key_file = 'encryption_key.key'

#Generate new fernet key
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key_file, key)

