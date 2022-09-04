message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if  ord("A") <= ord(ch) <= ord("Z"): 
        ch = chr(ord("A") + ((offset + ord(ch) - ord("A")) % 26))
        encoded_message = encoded_message + ch
    elif  ord("a") <= ord(ch) <=ord("z"):
        ch = chr(ord("a") + ((offset + ord(ch) - ord("a")) % 26))
        encoded_message = encoded_message + ch
    else:
        encoded_message = encoded_message + ch
print(encoded_message)
