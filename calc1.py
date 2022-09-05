result = None
operand = None
operator = None
wait_for_number = True
            
while True:
    if not result:
        result = input("Введи число: ")
        try:
            result = int(result)
            wait_for_number = False
        except ValueError:
            result = None
            continue
        
    if wait_for_number:
        operand = input("Введи число: ")
        try:
            operand = int(operand)
            wait_for_number = False
        except ValueError:
            continue
             
    if not wait_for_number and not operator:
        operator = input("Введи '+' или '-' или '/' или '*' или '=': ")
        if operator == "=" or '+' or '-' or '/' or '*':
            if operator == "=":
                print(f"Результат :=  {result}")
                break
            else:
                wait_for_number = True
                continue

    if wait_for_number == False and operator == "+":
        result = result + operand
        operator = None
        
    elif operator == "-":
        result = result - operand
        operator = None
        
    elif operator == "/":
        if operand != 0:
            result = result / operand
            operator = None
        else:
            print("Деление на ноль невозможно!")
            break

    elif operator == "*":
        result = result * operand
        operator = None
        

    else:
        continue
        
