pin_codes = ["0014", "0145", "0214", "2543"]

def is_valid_pin_codes(pin_codes):
    valid_pin_codes = True
    if not pin_codes: 
        valid_pin_codes = valid_pin_codes & False
    else:
        set_pin_codes = set(pin_codes)
        if len(set_pin_codes) != len(pin_codes):
            valid_pin_codes = valid_pin_codes & False            
        for pin in pin_codes:
            pin = str(pin)
            if len(pin) != 4:
                valid_pin_codes = valid_pin_codes & False
            else:
                try:
                    pin = int(pin)
                except ValueError:
                    valid_pin_codes = valid_pin_codes & False
                else:
                    valid_pin_codes = valid_pin_codes & True
    return valid_pin_codes
        
                
print(is_valid_pin_codes(pin_codes))
