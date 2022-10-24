def solve_riddle(riddle, word_length, start_letter, reverse=False):
    first = int(riddle.find(start_letter))
    word_length = int(word_length)
    last = word_length + first
    if first == -1:
        return word
    else:
        if reverse:
            last = first - word_length
            print(f'{first}:{last}:-1')
            return riddle[first:last:-1]
        else:
            last = word_length + first
            print(f'{first}:{last}')
            return riddle[first:last]

a = 'mi1powperet'
print(solve_riddle(a, 3, 'r', True))
print(a[8:5:-1])
