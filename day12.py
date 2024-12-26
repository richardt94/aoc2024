import sys
with open(sys.argv[1]) as f:
   garden_map = [l.strip() for l in f.readlines()]

max_y = len(garden_map)
max_x = len(garden_map[0])

def build_region(sx, sy):
   region = set()
   sides_r = {}
   sides_l = {}
   sides_t = {}
   sides_b = {}
   perimeter = 0
   target = garden_map[sy][sx]
   def dfs(x, y):
      nonlocal perimeter
      region.add((x,y))
      if x > 0 and garden_map[y][x - 1] == target:
         if (x - 1, y) not in region:
            dfs(x - 1, y)
      else:
         perimeter += 1
         if x not in sides_l:
            sides_l[x] = [y]
         else:
            sides_l[x].append(y)
      if y < max_y - 1 and garden_map[y + 1][x] == target:
         if (x, y + 1) not in region:
            dfs(x, y + 1)
      else:
         perimeter += 1
         if y + 1 not in sides_b:
            sides_b[y + 1] = [x]
         else:
            sides_b[y + 1].append(x)
      if x < max_x - 1 and garden_map[y][x + 1] == target:
         if (x + 1, y) not in region:
            dfs(x + 1, y)
      else:
         perimeter += 1
         if x + 1 not in sides_r:
            sides_r[x + 1] = [y]
         else:
            sides_r[x + 1].append(y)
      if y > 0 and garden_map[y - 1][x] == target:
         if (x, y - 1) not in region:
            dfs(x, y - 1)
      else:
         perimeter += 1
         if y not in sides_t:
            sides_t[y] = [x]
         else:
            sides_t[y].append(x)
      
   dfs(sx, sy)

   nsides = 0
   for side_x in sides_l:
      nsides += 1
      sorted_ys = sorted(sides_l[side_x])

      ny = sorted_ys[0]
      for edge_y in sorted_ys:
         if edge_y != ny:
            nsides += 1
            ny = edge_y + 1
         else:
            ny += 1
   for side_y in sides_t:
      nsides += 1
      sorted_xs = sorted(sides_t[side_y])

      nx = sorted_xs[0]
      for edge_x in sorted_xs:
         if edge_x != nx:
            nsides += 1
            nx = edge_x + 1
         else:
            nx += 1
   for side_x in sides_r:
      nsides += 1
      sorted_ys = sorted(sides_r[side_x])

      ny = sorted_ys[0]
      for edge_y in sorted_ys:
         if edge_y != ny:
            nsides += 1
            ny = edge_y + 1
         else:
            ny += 1
   for side_y in sides_b:
      nsides += 1
      sorted_xs = sorted(sides_b[side_y])

      nx = sorted_xs[0]
      for edge_x in sorted_xs:
         if edge_x != nx:
            nsides += 1
            nx = edge_x + 1
         else:
            nx += 1
   return region, perimeter, nsides
      
processed = set()
total_score = 0
total_score_sides = 0

for (sy, l) in enumerate(garden_map):
   for (sx, p) in enumerate(l):
      if (sx, sy) in processed:
         continue
      region, perimeter, nsides = build_region(sx, sy)
      print(len(region), perimeter, nsides)
      processed.update(region)
      total_score += len(region) * perimeter
      total_score_sides += len(region) * nsides

print(total_score, total_score_sides)
