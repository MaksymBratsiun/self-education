result = None
operand = None
operator = None
wait_for_number = True
while True:
    user_input = input(">>>")
    if user_input == "=":
        break
    elif wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print(f"'{user_input}' is not a number. Try again.")
            continue
        if result is None:
            result = operand
        elif operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            result /= operand
        wait_for_number = False
    else:
        if user_input in ('+', '-', '*', '/'):
            operator = user_input
        else:
            operator = None
        if operator is None:
            print(f"{user_input} is not '+' or '-' or '/' or '*'. Try again")
        else:
            wait_for_number = True
