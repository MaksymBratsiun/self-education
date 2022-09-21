terra = [[1, 1, 2, 10], [10, 2], [1, 1, 1]]
power = 1



def game(terra, power):
    i = 0
    j = 0
    for i in range(len(terra)):
        
        while j < len(terra[i]):
            if power >= terra[i][j]:
                power += terra[i][j]
                print(terra[i][j])
                print(f"pow={power}")
                j += 1
            else:
                i += 1
                j = 0
                break

game(terra, power)

