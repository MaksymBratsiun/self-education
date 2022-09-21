import re
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

print(articles_dict)
key = str(input("input key: "))

def find_articles(key, letter_case=True):
    title = ""
    author = ""
    find_dict = []

    if letter_case:
                
        for dict in articles_dict:
            
            title = dict["title"]
            author = dict["author"]       
            print(title, key, title.find(key))
            print(author, key, author.find(key))
            if title.find(key) != -1 or author.find(key) != -1:
                
                find_dict.append(dict)
        
    else:

        key = key.lower()
                
        for dict in articles_dict:

            title = dict["title"]
            author = dict["author"]
            title = title.lower()
            author = author.lower()
            
            print(title, key, title.find(key))
            print(author, key, author.find(key))
            if title.find(key) != -1 or author.find(key) != -1:
                print(find_dict)
                
                find_dict.append(dict)

    return find_dict
            
    
print("\n\n", find_articles(key))      



    
