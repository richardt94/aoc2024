import sys

with open(sys.argv[1]) as f:
   antenna_map = f.readlines()

max_y = len(antenna_map) - 1
max_x = len(antenna_map[0]) - 2

antennas = {}

for (y, line) in enumerate(antenna_map):
   for (x, ch) in enumerate(line):
      if ch == '.' or ch == '\n':
         continue
      if ch in antennas:
         antennas[ch].append((x,y))
      else:
         antennas[ch] = [(x,y)]

anodes = set()
anodes_all = set()
for ch in antennas:
   for a1 in antennas[ch]:
      if a1[0] < 0 or a1[0] > max_x or a1[1] < 0 or a1[1] > max_y:
         print(a1)
      for a2 in antennas[ch]:
         dx = a2[0] - a1[0]
         dy = a2[1] - a1[1]
         if dx == 0 and dy == 0:
            continue
         tl = (a2[0] + dx, a2[1] + dy)
         if (tl[0] >= 0 and tl[1] >= 0 and tl[0] <= max_x and tl[1] <= max_y):
            anodes.add(tl)
         
         tl = a1
         while (tl[0] >= 0 and tl[1] >= 0 and tl[0] <= max_x and tl[1] <= max_y):
            anodes_all.add(tl)
            tl = (tl[0] + dx, tl[1] + dy)
 

print(len(anodes))
print(len(anodes_all))
