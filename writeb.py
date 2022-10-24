users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
list_users = []
string = ''
    
for user, password in users_info.items():
    print(user, password)
    string = (user + ': ' + password).encode()
    list_users.append(string)
    list_users.append(b'\n')
    
with open('1.bin', 'wb') as file:
    file.writelines(list_users)
    
with open('1.bin', 'rb') as file1:
    print(file1.readlines())


