import sys

with open(sys.argv[1]) as f:
   sizes = f.read()

disk_map = []
free_blocks = []
files = []
for (i,s) in enumerate(sizes.strip()):
   if i % 2 == 0:
      id = i // 2
      files.append((len(disk_map), int(s), id))
      for _ in range(int(s)):
         disk_map.append(id)
   else:
      free_blocks.append((len(disk_map), int(s)))
      for _ in range(int(s)):
         disk_map.append(-1)
      
  
print(disk_map)
print(files)
print(free_blocks)

ptr_start = 0

while disk_map[ptr_start] >= 0:
   ptr_start += 1

ptr_end = len(disk_map) - 1
while disk_map[ptr_end] < 0:
   ptr_end -= 1

while ptr_end > ptr_start: 
   disk_map[ptr_start] = disk_map[ptr_end]
   disk_map[ptr_end] = -1
   while disk_map[ptr_start] >= 0:
      ptr_start += 1
   while ptr_end >= 0 and disk_map[ptr_end] < 0: 
      ptr_end -= 1

print(disk_map) 

print(sum([i * j if j > 0 else 0 for (i,j) in enumerate(disk_map)]))

for start, length, id in files[::-1]:
   for i, (fstart, flength) in enumerate(free_blocks):
      if fstart >= start:
         break
      if flength >= length:
         files[id] = (fstart, length, id)
         free_blocks[i] = (fstart + length, flength - length)
         break

disk_map_contiguous = []
for (start, length, id) in sorted(files):
   while len(disk_map_contiguous) < start:
      disk_map_contiguous.append(-1)
   disk_map_contiguous.extend([id] * length)

print(disk_map_contiguous)
print(sum([i * j if j > 0 else 0 for (i,j) in enumerate(disk_map_contiguous)]))  
