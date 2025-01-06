import sys

with open(sys.argv[1]) as f:
   hiking_map = f.readlines()

num_routes = 0
num_ends = 0
visited = set()
def dfs(x, y):
   global num_routes, visited, num_ends
   if hiking_map[y][x] == '9':
      if (x, y) not in visited:
         num_ends += 1
         visited.add((x,y))
      num_routes += 1
      return
   
   for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
      if nx < len(hiking_map[0]) - 1 and nx >= 0 and ny < len(hiking_map) and ny >= 0:
         if int(hiking_map[ny][nx]) - int(hiking_map[y][x]) == 1:
            dfs(nx, ny)

for y, line in enumerate(hiking_map):
   for x, ch in enumerate(line):
      if ch == '0':
         visited = set()
         dfs(x, y)

print(num_ends)
print(num_routes)
   
