def sanitize_phone_number(phone):
    not_num = [" ", "(", ")", "+", "-"]
    sanitize_phone = ""
    phone = phone.strip()
    for char in phone:
        if char in not_num:
            continue
        else:
            sanitize_phone += char
    return sanitize_phone


def get_phone_numbers_for_countries(list_phones):
    
    phone_countries = {}
    phone_ua = []
    phone_jp = []
    phone_tw = []
    phone_sg = []

    print(list_phones)
    
    for phone in list_phones:

        sanitize_phone_number(phone)
        
        print(phone)
        
        phone = str(phone)
        
        if phone.startswith("81"):
            phone_jp.append(phone)
        
        elif phone.startswith("886"):
            phone_tw.append(phone)
        
        elif phone.startswith("65"):
            phone_sg.append(phone)
        
        else:
            phone_ua.append(phone)
        
    phone_countries.update({"UA":phone_ua})
    phone_countries.update({"JP":phone_jp})
    phone_countries.update({"TW":phone_tw})
    phone_countries.update({"SG":phone_sg})

    return phone_countries
