import sys
with open(sys.argv[1]) as f:
   data = f.read()

locks_or_keys = data.split("\n\n")

locks = []
keys = []
for l_k in locks_or_keys:
   rows = l_k.split("\n")
   if rows[0][0] == '#':
      heights = [5,5,5,5,5]
      for col in range(5):
         for row in range(5):
            if rows[row + 1][col] == '.':
               heights[col] = row
               break
      locks.append(heights)
   else:
      heights = [5,5,5,5,5]
      for col in range(5):
         for row in range(5):
            if rows[5 - row][col] == '.':
               heights[col] = row
               break
      keys.append(heights)

print(locks, keys)

n_pairs = 0
for lock in locks:
   for key in keys:
      for h1, h2 in zip(lock, key):
         if h1 + h2 > 5:
            break
      else:
         n_pairs += 1

print(n_pairs)