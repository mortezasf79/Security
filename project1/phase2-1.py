
from cryptography.fernet import Fernet

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)


key = load_key()
encrypt("file.txt", key=key)