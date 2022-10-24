def all_sub_lists(data):
    print(data)   
    new_data = [[]]
    data_s = []
    
    def sub_list(data_n):
        n = len(data_n)
        if n == 1:
            new_data.append(data_n)                   
        else:
            new_data.append(data_n[0:n-1])
            sub_list(data_n[0:n-1])
            new_data.append(data_n[1:n])
            sub_list(data_n[1:n])
    
    sub_list(data)
    for item in new_data:
        if item not in data_s:
            data_s.append(item)
    print(data_s)
    data_s.append(data)
    
    
    return data_s
