import sys

with open(sys.argv[1]) as f:
    map = f.readlines()

xmas_dict = {
    'X' : 'M',
    'M' : 'A',
    'A' : 'S'
}

def dfs(x, y, cs):
    if x < 0 or x >= len(map[0]):
        return 0
    if y < 0 or y >= len(map):
        return 0
    
    if cs == 'S':
        return map[y][x] == 'S'
    elif map[y][x] == cs:
        cn = xmas_dict[cs]
        num_occurrences = 0
        for ny in [y - 1, y, y + 1]:
            for nx in [x - 1, x, x + 1]:
                if nx == x and ny == y:
                    continue
                num_occurrences += dfs(nx, ny, cn)
        return num_occurrences
    else:
        return 0

total = 0
for sy in range(len(map)):
    for sx in range(len(map[0])):
        occ = dfs(sx, sy, 'X')
        # print(sx, sy, occ)
        total += occ

print(total)

total = 0
for sy in range(len(map)):
    for sx in range(len(map[0])):
        if map[sy][sx] != 'X':
            continue
        test = ('M', 'A', 'S')

        l = sx >= 3
        r = sx < len(map) - 3

        if sy < len(map) - 3:
            # down
            if (map[sy + 1][sx], map[sy + 2][sx], map[sy + 3][sx]) == test:
                total += 1
            
            # down-left
            if l and (map[sy + 1][sx - 1], map[sy + 2][sx - 2], map[sy + 3][sx - 3]) == test:
                total += 1
            
            # down-right
            if r and (map[sy + 1][sx + 1], map[sy + 2][sx + 2], map[sy + 3][sx + 3]) == test:
                total += 1
        
        if sy >= 3:
            # up
            if (map[sy - 1][sx], map[sy - 2][sx], map[sy - 3][sx]) == test:
                total += 1
            
            # up-left
            if l and (map[sy - 1][sx - 1], map[sy - 2][sx - 2], map[sy - 3][sx - 3]) == test:
                total += 1
            
            # up-right
            if r and (map[sy - 1][sx + 1], map[sy - 2][sx + 2], map[sy - 3][sx + 3]) == test:
                total += 1
        
        # left
        if l and (map[sy][sx - 1], map[sy][sx - 2], map[sy][sx - 3]) == test:
            total += 1
        
        # right
        if r and (map[sy][sx + 1], map[sy][sx + 2], map[sy][sx + 3]) == test:
            total += 1

total_x = 0
for sy in range(1, len(map) - 1):
    for sx in range(1, len(map[0]) - 1):
        if map[sy][sx] == 'A':
            if (map[sy - 1][sx - 1] == 'M' and map[sy + 1][sx + 1] == 'S') or (map[sy - 1][sx - 1] == 'S' and map[sy + 1][sx + 1] == 'M'):
                if (map[sy - 1][sx + 1] == 'M' and map[sy + 1][sx - 1] == 'S') or ((map[sy - 1][sx + 1] == 'S' and map[sy + 1][sx - 1] == 'M')):
                    total_x += 1

print(total)
print(total_x)
