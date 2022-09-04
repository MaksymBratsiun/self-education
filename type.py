name = input("What is your name?: ")
string_hello = f"Nice to meet you{name}!"
age = input(f"How old are you? {name}: ")
try:
    age = int(age)
    if age >= 18:
        print("You are adult.")
    else:
        print("You are infant")
except ValueError:
    print(f"{age} is not a number")
home_town = "Kharkiv"
city = input("Where are you from?: ")
if city == home_town:
    print (f"I am from Kharkiv too!")

