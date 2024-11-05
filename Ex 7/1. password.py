import re

def password_validity(password):
    # The updated regular expression pattern
    pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[A-Za-z0-9!@#$%^&*]{6,10}$'
    if re.search(pattern, password):
        print("The password is valid")
    else:
        print("The password is not valid")

if __name__ == "__main__":
    password_validity("S1*3a7&a7")
    password_validity("AbCdEfGhI123") 
    password_validity("!@#$%^&*")     
    password_validity("Ab1234$%^")   
    password_validity("ABC123!@#")
