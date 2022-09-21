points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

coordinates = [0, 2, 3, 2, 0, 3, 2, 0]


def calculate_distance(coordinates):
    len_coordinates = len(coordinates)
    distance = 0
    if len_coordinates < 2:
        return 0
    path_run = coordinates[0:2]
    for i in range(len_coordinates - 1):
        path_run = coordinates[i:i+2]
        path_run.sort()
        path_run = tuple(path_run)
        distance += points[path_run]
    return distance


print(calculate_distance(coordinates))


    
  
