import sys
from collections import deque

sys.setrecursionlimit(10000)

with open(sys.argv[1]) as f:
   racetrack = [l.strip() for l in f.readlines()]

for y, line in enumerate(racetrack):
   for x, ch in enumerate(line):
      if ch == 'S':
         sy, sx = (y, x)
      elif ch == 'E':
         ty, tx = (y, x)

q = deque([(0, sy, sx)])
sp_to = {}
while len(q):
   dt, y, x = q.popleft()
   if (y, x) in sp_to:
      continue
   sp_to[(y,x)] = dt
   for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      ny, nx = y + d[0], x + d[1]
      if racetrack[ny][nx]=='#':
         continue
      q.append((dt + 1, ny, nx))

q = deque([(0, ty, tx)])
sp_from = {}
while len(q):
   dt, y, x = q.popleft()
   if (y, x) in sp_from:
      continue
   sp_from[(y,x)] = dt
   for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      ny, nx = y + d[0], x + d[1]
      if racetrack[ny][nx]=='#':
         continue
      q.append((dt + 1, ny, nx))

sp = sp_to[(ty, tx)]

savings = [0] * (sp + 1)
for cs in sp_to:
   len_to = sp_to[cs]
   for dy in range(-20, 20 + 1):
      for dx in range(-20 + abs(dy), 20 - abs(dy) + 1):
         ce = (cs[0] + dy, cs[1] + dx)
         if ce in sp_from:
            saving = sp - sp_from[ce] - sp_to[cs] - abs(dy) - abs(dx)
            if saving > 0:
               savings[saving] += 1

print(sum(savings[100:]))
