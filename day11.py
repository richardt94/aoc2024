import sys
with open(sys.argv[1]) as f:
   stones = f.read().strip().split()

nblinks = 25

for i in range(nblinks):
   nstones = []
   for stone in stones:
      if int(stone) == 0:
         nstones.append('1')
      elif len(stone) % 2 == 0:
         nstones.append(stone[:len(stone) // 2])
         nstones.append(str(int(stone[len(stone) // 2:])))
      else:
         nstones.append(str(int(stone) * 2024))
   
   stones = nstones
   print(i + 1, len(stones))

print(len(stones))

dp = {}
def num_stones(stone, nblinks):
   if (stone, nblinks) not in dp:
      if nblinks == 0:
         dp[(stone, nblinks)] = 1
      elif stone == 0:
         dp[(stone, nblinks)] = num_stones(1, nblinks - 1)
      elif len(str(stone)) % 2 == 0:
         ss = str(stone)
         dp[(stone, nblinks)] = num_stones(int(ss[:len(ss) // 2]), nblinks - 1) + num_stones(int(ss[len(ss) // 2:]), nblinks - 1)
      else:
         dp[(stone, nblinks)] = num_stones(stone * 2024, nblinks - 1)
   return dp[(stone, nblinks)]

total = 0
with open(sys.argv[1]) as f:
   stones = f.read().strip().split()

nblinks = 75
for s in stones:
   total += num_stones(int(s), nblinks)

print(total)

  
