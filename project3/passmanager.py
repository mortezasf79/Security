from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
from cryptography.fernet import Fernet
import argparse


def encrypt_password(key, password):
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password


def decrypt_password(key, encrypted_password):
    cipher_suite = Fernet(key)
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password



def save_password(name, password, description, filename):
    data = {
        'name': name,
        'password': password,
        'description': description
    }
    with open(filename, 'a') as file:
        json.dump(data, file)
        file.write('\n')

def load_passwords(filename):
    passwords = []
    with open(filename, 'r') as file:
        for line in file:
            password = json.loads(line)
            passwords.append(password)
    return passwords


def load_password(name, filename , key):
    passwords = load_passwords(filename)
    for password in passwords :
        if password['name'] == name:
            print(f'Name:' + name 
                  + "\n" f'Password: ' + decrypt_password(key, password['password'])
                  + "\n" + f'Description: ' +  password['description'] + "\n") 


def show_names(filename):
    passwords = load_passwords(filename)
    print("List of names:")
    for password in passwords:
        print(password['name'])
    print()


def update_password(name, newPass, key,filename ):
    passwords = load_passwords(filename)
    for password in passwords:
        if password['name'] == name:
            password['password'] = encrypt_password(key ,newPass).decode()
            break
    # ذخیره رمزهای جدید در فایل
    with open(filename, 'w') as file:
        for password in passwords:
            json.dump(password, file)
            file.write('\n')


def delete_password(name, filename):
    # بارگیری رمزها از فایل
    passwords = load_passwords(filename)
    
    
    # جستجو و حذف رکورد مورد نظر
    for password in passwords:
        if password['name'] == name:
            passwords.remove(password)
            break
    
    # ذخیره رمزهای جدید در فایل
    with open(filename, 'w') as file:
        for password in passwords:
            json.dump(password, file)
            file.write('\n')




def create_argument_parser():
    parser = argparse.ArgumentParser(prog='passmanager.py', description='Password Manager')

    subparsers = parser.add_subparsers(dest='command', title='Commands')

    # Command: newpass
    newpass_parser = subparsers.add_parser('newpass', help='Create a new password')
    newpass_parser.add_argument('name', help='Name of the password')
    newpass_parser.add_argument('-c', '--comment', help='Comment for the password')
    newpass_parser.add_argument('-key', '--password', help='User simple password')

    # Command: --showpass
    subparsers.add_parser('showpass', help='Show saved passwords')

    # Command: --sel
    sel_parser = subparsers.add_parser('sel', help='Show password value and comment')
    sel_parser.add_argument('name', help='Name of the password')

    # Command: --update
    update_parser = subparsers.add_parser('update', help='Update password value')
    update_parser.add_argument('name', help='Name of the password')
    update_parser.add_argument('-key', '--password', help='User new password')

    # Command: --del
    del_parser = subparsers.add_parser('del', help='Delete a password')
    del_parser.add_argument('name', help='Name of the password')

    return parser





def main():
    
    key = b't_-wUtK2eEXoPHyQxRRL_x0typzZi1IQhzk_GxLsH_E='

    filename = "passInformation.json"

    # name = "portal1"
    # pass1 = "salam"
    # description = "123456"

    # cipherText = encrypt_password(key ,pass1).decode()
    # print(cipherText)


    # save_password(name, cipherText , description, filename)


    # update_password("portal1", "1234" , key , filename= filename)


    # load_password("portal1" , filename , key)


    # delete_password("portal1", "passInformation.json")


    # retrieved_passwords = load_passwords(filename)
    # # چاپ پسوردها
    # for password in retrieved_passwords:
    #     print(f"name: {password['name']}")
    #     print(f"password: {password['password']}")
    #     print(f"description: {password['description']}")
    #     print()


    parser = create_argument_parser()
    args = parser.parse_args()

    if args.command == 'newpass':
        # Handle newpass command
        print(f'Creating new password: Name={args.name}, Comment={args.comment}, Key={args.password}')
        cipherText = encrypt_password(key ,args.password).decode()
        save_password(args.name, cipherText , args.comment, filename)
        print("Password created succussfully.")

    elif args.command == 'showpass':
        # Handle showpass command
        print()
        print('Showing saved passwords')
        show_names(filename)

    elif args.command == 'sel':
        # Handle sel command
        print()
        print(f'Showing password value and comment for: Name={args.name}')
        load_password(args.name,filename,key)

    elif args.command == 'update':
        # Handle update command
        print()
        print(f'Updating password value for: Name={args.name}')
        update_password(args.name, args.password , key , filename= filename)
        print()

    elif args.command == 'del':
        # Handle del command
        print()
        print(f'Deleting password: Name={args.name}')
        delete_password(args.name, filename)
        print()


 

if __name__ == "__main__":
    main()