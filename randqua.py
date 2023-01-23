from random import randrange


def get_numbers_ticket(min, max, quantity):
    set_num = set()
    if int(min) < 1:
        return [] 
    elif int(max) >=1000:
        return []
    elif int(min) > int(max):
        return []
    elif int(quantity) < int(min) or int(quantity) > int(max):
        return []
    else:
        while len(set_num) < int(quantity):
             set_num.add(randrange(int(min), int(max)+1))

    list_num = list(set_num)
    list_num.sort()
    return list_num

print(get_numbers_ticket(2, 15, 6))
