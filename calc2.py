operand = None
operator = None
result = None
wait_for_number = True

while True:
    
    while not result:
        try:
            operand = input("Введите число: ")
            operand = int(operand)
        except ValueError:
            print(f"{operand} не число. Введите число: ")
        else:
            result = operand
            break
        
    while True:
        operator = input("Введите оператор '+' или '-' или '/' или '*' или '=': ")
        if operator not in ("+", "-", "*", "/", "="):
            print(f"{operator} - не оператор. Введите оператор: ")
        else:
            break
        
    while operator != "=":
        try:
            operand = input("Введите число: ")
            operand = int(operand)
        except ValueError:
            print(f"{operand} не число. Введите число: ")
        else:
            break
        
    if operator == "+":
        result += operand
    elif operator == "-":
        result -= operand
    elif operator == "*":
        result *= operand
    elif operator == "/":
        try:
            result /= operand
        except ZeroDivisionError:
            print(f" Деление на ноль! Ваш результат до деления := {result}")
            break
    elif operator == "=":
        print(f"Ваш результат := {result}")
        break
