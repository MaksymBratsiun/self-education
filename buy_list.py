buy_list = "Your buy list:\n"

print("What do yo want to buy or say 'stop': ")

while True:
   
    buy_list_new = input("What do you want to buy:")

    if buy_list_new == "stop":
        print(buy_list)
        break

    buy_list = buy_list + buy_list_new + "\n"
    
    
 
    
