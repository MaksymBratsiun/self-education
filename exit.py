
count = 0
while True:
    u = input()
    if not u.find(".") == -1:
        print(". in text")
        quit()
    else:
        print("do somesing")
    count += 1
    if count > 10:
        break
