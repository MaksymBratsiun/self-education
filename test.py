import sys

def parse_args():
    result = ""
    masiv = []

    for arg in sys.argv:
        print(arg)
        masiv.append(arg)
    
    masiv.pop(0)
    result = " ".join(masiv)   
    print(masiv)    
    return result
            
        
print(parse_args())
