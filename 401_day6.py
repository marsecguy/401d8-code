#!/usr/bin/python3

#In Python, create a script that utilizes the cryptography library to:

#Prompt the user to select a mode:
    #Encrypt a file (mode 1)
    #Decrypt a file (mode 2)
    #Encrypt a message (mode 3)
    #Decrypt a message (mode 4)
#If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.
#If mode 3 or 4 are selected, prompt the user to provide a cleartext string.
#Depending on the selection, perform one of the below functions. You’ll need to create four functions:
    #Encrypt the target file if in mode 1.
        #Delete the existing target file and replace it entirely with the encrypted version.
    #Decrypt the target file if in mode 2.
        #Delete the encrypted target file and replace it entirely with the decrypted version.
#Encrypt the string if in mode 3.
#Print the ciphertext to the screen.
#Decrypt the string if in mode 4.
#Print the cleartext to the screen.

# Import libraries
from cryptography.fernet import Fernet
import os

# Define functions

    # Function to generate key and save it to a file: "key_file"
def write_key():
    key = Fernet.generate_key()
    f = Fernet(key)
    with open("key.key","wb") as key_file:
        key_file.write(key)

    # Function to load the key
def use_key():
    return open("key.key", "rb").read()


    # Function to encrypt a file with the key
def encrypt_file(file_path):
    key = use_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

# Function to decrypt a file

# Function to encrypt a message 
