import sys
with open(sys.argv[1]) as f:
   warehouse = f.read()

wmap, moves = warehouse.split("\n\n")

wmap = wmap.split("\n")

boxes = set()
walls = set()
for y, line in enumerate(wmap):
   for x, ch in enumerate(line):
      if ch == '@':
         rpos = (x, y)
      elif ch == 'O':
         boxes.add((x,y))
      elif ch == '#':
         walls.add((x,y))



for move in moves:
   if move == '<':
      dpos = (-1, 0)
   elif move == '>':
      dpos = (+1, 0)
   elif move == 'v':
      dpos = (0, +1)
   elif move == '^':
      dpos = (0, -1)
   else:
      continue
   
   nrpos = (rpos[0] + dpos[0], rpos[1] + dpos[1])

   to_move = []
   test_pos = nrpos
   while test_pos in boxes:
      to_move.append(test_pos)
      test_pos = (test_pos[0] + dpos[0], test_pos[1] + dpos[1])
   if test_pos in walls:
      continue

   for box in to_move:
      boxes.remove(box)
   for box in to_move:
      boxes.add((box[0] + dpos[0], box[1] + dpos[1]))

   rpos = nrpos

GPS_total = 0
for y in range(len(wmap)):
   for x in range(len(wmap[0])):
      if (x, y) in walls:
         print('#', end='')
      elif (x, y) in boxes:
         print('O', end='')
         GPS_total += 100 * y + x
      elif rpos == (x, y):
         print('@', end='')
      else:
         print('.', end='')
   print()

print(GPS_total)
print()

boxes = set()
walls = set()
for y, line in enumerate(wmap):
   for x, ch in enumerate(line):
      if ch == '@':
         rpos = (2 * x, y)
      elif ch == 'O':
         boxes.add((2 * x,y))
      elif ch == '#':
         walls.add((2 * x,y))

to_move = set()
def push(x, y, d):
   if (x, y + d) in walls or (x + 1, y + d) in walls or (x - 1, y + d) in walls:
      return False
 
   if (x, y + d) in boxes:
      if not push(x, y + d, d):
         return False
   else:
      if (x - 1, y + d) in boxes:
         if not push(x - 1, y + d, d):
            return False
      if (x + 1, y + d) in boxes:
         if not push(x + 1, y + d, d):
            return False
   to_move.add((x, y))
   return True


def pwar():
   GPS_total = 0
   for y in range(len(wmap)):
      for x in range(0, 2 * len(wmap[0])):
         if (x, y) in walls or (x - 1, y) in walls:
            print('#', end='')
         elif (x, y) in boxes:
            GPS_total += 100 * y + x
            print('[', end='')
         elif (x - 1, y) in boxes:
            print(']', end='')
         elif rpos == (x, y):
            print('@', end='')
         else:
            print('.', end='')
      print()
   print(GPS_total)
   print()

for i, move in enumerate(moves):
   to_move = set()
   if move == 'v' or move == '^':
      d = 1 if move == 'v' else -1
      nrpos = (rpos[0], rpos[1] + d)
      if nrpos in walls or (nrpos[0] - 1, nrpos[1]) in walls:
         continue
      if nrpos in boxes:
         if push(*nrpos, d):
            for box in to_move:
               boxes.remove(box)
            for box in to_move:
               boxes.add((box[0], box[1] + d))
            rpos = nrpos
         continue
      if (nrpos[0] - 1, nrpos[1]) in boxes:
         if push(nrpos[0] - 1, nrpos[1], d):
            for box in to_move:
               boxes.remove(box)
            for box in to_move:
               boxes.add((box[0], box[1] + d))
            rpos = nrpos
         continue
      rpos = nrpos
      continue

   if move == '<':
      d = -1
   elif move == '>':
      d = +1
   else:
      continue
   
   nrpos = (rpos[0] + d, rpos[1])

   test_pos = nrpos if d == 1 else (nrpos[0] - 1, nrpos[1])
   while test_pos in boxes:
      to_move.add(test_pos)
      test_pos = (test_pos[0] + 2 * d, test_pos[1])
   if test_pos in walls:
      continue

   for box in to_move:
      boxes.remove(box)
   for box in to_move:
      boxes.add((box[0] + d, box[1]))

   rpos = nrpos

  
pwar()
