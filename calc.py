result = None
operand = None
operator = None
wait_for_number = True
            
while True:
    if result == None:
        result = input("Введи число: ")
        operand = 0
        try:
            result = int(result)
            wait_for_number = False
            print(f" цикл ввода ервого числа {result}{operand}")
        except ValueError:
            result = None
            continue
        
    if wait_for_number == True:
        operand = input("Введи число: ")
        try:
            operand = int(operand)
            wait_for_number = False
        except ValueError:
            continue
             
    if wait_for_number == False:
        operator = input("Введи '+' или '-' или '/' или '*' или '=': ")
        print(f" цикл ввода оператора {result}{operand}")
        if operator == "=" or '+' or '-' or '/' or '*':
            if operator == "=":
                print(f"Результат :=  {result}")
                break
            else:
                if operator == "+":
                    result = result + operand
                    wait_for_number = True
                elif operator == "-":
                    result -= operand
                    wait_for_number = True
                elif operator == "/":
                    result /= result / operand
                    wait_for_number = True
                elif operator == "*":
                    result *= operand
                    wait_for_number = True
        else:
            continue
