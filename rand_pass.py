from random import randint

def get_random_password():

    password = ""
    for  _ in range(8):
        random_num = randint(40, 126)
        password += chr(random_num)
    return password

def is_valid_password(password):

    valid_password = True
    up_valid = False
    low_valid = False
    num_valid = False

    if len(password) < 8:
        valid_password = valid_password & False
    
    for char in password:
        if "a" <= char <= "z":
            up_valid = True
        if "A" <= char <= "Z":
            low_valid = True
        if "0" <= char <= "9":
            num_valid = True
    
    if up_valid & low_valid & num_valid: 
         valid_password = valid_password & True
    else:
        valid_password = valid_password & False

    return valid_password

def get_password():
    try_get_pass = 100
    password = ""
    while try_get_pass > 0:
        try_get_pass -= 1    
        password = get_random_password()
        if is_valid_password(password):
             return password, try_get_pass 
             break
    
        
        

password = get_password()
print(password)

