import re

def check_password_strength(password):
    if len(password) < 8:
        return "Password should be have at least 8 character..."
    
    with open('dictionary.txt', 'r') as f:
        dictionary = f.read().splitlines()
        
    if password in dictionary:
        return "This password is common and cannot be accepted..."
    
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return "Password should contain uppercase and lowercase letters..."
    
    if not re.search(r'\d', password):
        return "Password should contain 1 or more digit..."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', password):
        return "Password must contain symbols..."
    

    

    return "Password is strength."

password = input("Please enter your password: ")
result = check_password_strength(password)
print(result)