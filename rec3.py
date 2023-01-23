def flatten(data):

    if not (bool(data)):
        return data
    print(f'снаружи {data}')
   
    if isinstance(data[0], list):
        print(f' внутри {data}')
        
        return flatten(*data[0:1]) + flatten(data[1:])

    return data[:1] + flatten(data[1:])


data = [1, 2, [3, 4, [5, 6]], 7]

print(flatten(data))