import re

def real_len(text):
    rule_sumbol = re.findall('\s', text)
    real_len = len(text) - len(rule_sumbol)
    return real_len
    
text = 'Al\nKdfe23\t\v.\r\n'
print(real_len(text))

            
        
    
