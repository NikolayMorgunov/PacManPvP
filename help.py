with open("full_map.txt", 'r') as file:
    s = file.read().split('\n')


with open("walls.txt", 'w') as file:
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == '#':
                file.write('(' + str(i) + ', ' + str(j) + ')\n')
