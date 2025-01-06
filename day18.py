import sys
from collections import deque

with open(sys.argv[1]) as f:
   bytes = f.readlines()

maxx, maxy = (70, 70)

blocks = set()

for byte in bytes[:1024]:
   x, y = [int(c) for c in byte.split(",")]
   blocks.add((x, y))

q = deque()
q.append((0, 0, 0))

visited = [[0 for _ in range(maxy + 1)] for _ in range(maxx + 1)]
while len(q):
   dt, x, y = q.popleft()
   if visited[x][y]:
      continue
   visited[x][y] = 1
   if x == maxx and y == maxy:
      print(dt)
      break
   for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
      if nx > maxx or nx < 0 or ny < 0 or ny > maxy:
         continue
      if (nx, ny) in blocks:
         continue
      q.append((dt + 1, nx, ny))

# blocks = set()
# shortest_path = None
# for last_byte in range(len(bytes)):
#    bx, by = [int(c) for c in bytes[last_byte].split(",")]
#    blocks.add((bx, by))
#    
#    if shortest_path is None or (bx, by) in shortest_path: 
# 
#       visited = [[0 for _ in range(maxy + 1)] for _ in range(maxx + 1)]
#       q = deque([(0, 0, 0, [])])
#       while len(q):
#          dt, x, y, sp = q.popleft()
#          if visited[x][y]:
#             continue
#          visited[x][y] = 1
#          if x == maxx and y == maxy:
#             shortest_path = sp
#             break
#          for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#             if nx > maxx or nx < 0 or ny < 0 or ny > maxy:
#                continue
#             if (nx, ny) in blocks:
#                continue
#             q.append((dt + 1, nx, ny, sp + [(x, y)]))
#       else:
#          print(f"{bx},{by}")
#          break
# 
blocks = set()

for byte in bytes:
   bx, by = [int(c) for c in byte.split(",")]
   blocks.add((bx, by))

def bfs(start_node, disjoint_sets=[]):
   q = deque([start_node])
   visited = set()

   while len(q):
      x, y = q.popleft()
      if (x, y) in visited:
         continue
      visited.add((x, y))
      for s in disjoint_sets:
         if (x, y) in s:
            visited = visited.union(s)
      for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
         if (nx, ny) in blocks:
            continue
         if nx > maxx or nx < 0 or ny < 0 or ny > maxy:
            continue
         q.append((nx, ny))
   return visited

disjoint_sets = []

for start_node in [(0, 0), (maxx, maxy)]:
   disjoint_sets.append(bfs(start_node))

for byte in bytes[::-1]:
   bx, by = [int(c) for c in byte.split(",")]
   blocks.remove((bx, by))
   new_set = bfs((bx, by), disjoint_sets=disjoint_sets)
   nd = []
   for d in disjoint_sets:
      if len(d.difference(new_set)) == 0:
         continue
      else:
         nd.append(d)
   nd.append(new_set)
   
   if (0,0) in new_set and (maxx, maxy) in new_set:
      print(f"{bx},{by}")
      break
