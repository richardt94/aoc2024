import sys
import heapq

with open(sys.argv[1]) as f:
   maze = [l.strip() for l in f.readlines()]


walls = set()
for y, l in enumerate(maze):
   for x, ch in enumerate(l):
      if maze[y][x] == 'S':
         state = (x, y, 0)
      elif maze[y][x] == 'E':
         tpos = (x, y)
      elif maze[y][x] == '#':
         walls.add((x, y))


stack = [(0, *state, [])]

dt = -1
seats = set()
visited = set()
while len(stack) > 0:
   dist_to_test, tx, ty, td, path = heapq.heappop(stack)
   visited.add((tx, ty, td))
   if (tx, ty) == tpos:
      if dt < 0:
         dt = dist_to_test
      if dist_to_test == dt:
         seats = seats.union(path)
      continue
   
   for nd in [(td - 1) % 4, (td + 1) % 4]:
      if (tx, ty, nd) not in visited:
         heapq.heappush(stack, (dist_to_test + 1000, tx, ty, nd, path))
   
   movement = ((td % 2 == 0) * (1 - td), (td % 2) * (2 - td))

   nx, ny = (tx + movement[0], ty + movement[1])

   if (nx, ny) in walls:
      continue
      
   if (nx, ny, td) not in visited:
      npath = path.copy()
      npath.append((tx, ty))
      heapq.heappush(stack, (dist_to_test + 1, nx, ny, td, npath))


print(dt)
print(len(seats) + 1)
