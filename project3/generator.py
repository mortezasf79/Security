import hashlib

from cryptography.fernet import Fernet


def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

def constant_hash(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    
    return md5_hash


def main():

    key = b't_-wUtK2eEXoPHyQxRRL_x0typzZi1IQhzk_GxLsH_E='
    text = "0000"


    for i in range(10000):
        print(i)
        
        text = constant_hash(text)
        with open('test.txt', 'a') as file:
            file.write(text + "\n")


if __name__ == "__main__":
    main()