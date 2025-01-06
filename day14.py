import sys, re
from time import sleep
from math import gcd

robot_rgx = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"

with open(sys.argv[1]) as f:
   matches = re.findall(robot_rgx, f.read())

q = [0,0,0,0]
for m in matches:
   x, y, vx, vy = [int(g) for g in m]
   x += 100 * vx
   y += 100 * vy
   x %= 101
   y %= 103
   if x == 101// 2 or y == 103 // 2:
      continue
   quad = (x > 101 // 2) + 2 * (y > 103 // 2)
   q[quad] += 1

total = q[0]
for qu in q[1:]:
   total *= qu

print(total)

pos = {}


istep_horizontal = 86
dstep_horizontal = 101

istep_vertical = 57
dstep_vertical = 103

dstep = dstep_vertical * dstep_horizontal // gcd(dstep_vertical, dstep_horizontal)
istep = istep_vertical
while (istep - istep_horizontal) % dstep_horizontal != 0:
   istep += dstep_vertical

for m in matches:
   v = (int(m[2]), int(m[3]))
   x = ((int(m[0]) + v[0] * istep) % 101, (int(m[1]) + v[1] * istep) % 103)
   if x in pos:
      pos[x].append(v)
   else:
      pos[x] = [v]

i = istep
while True:
   print(i)
   for y in range(103):
      for x in range(101):
         if (x,y) in pos:
            print('#', end='')
         else:
            print(' ', end='')
      print()
   npos = {}
   print()
   for x in pos:
      for v in pos[x]:
         nx = ((x[0] + dstep * v[0]) % 101, (x[1] + dstep * v[1]) % 103)
         if nx in npos:
            npos[nx].append(v)
         else:
            npos[nx] = [v]
   pos = npos 
   i += dstep
   sleep(2)
