import sys

with open(sys.argv[1]) as f:
   lab_map = f.readlines()

start = (-1, -1)

max_y = len(lab_map)
max_x = len(lab_map[0]) - 1

blocks = set()

for y in range(max_y):
	for x in range(max_x):
		if lab_map[y][x] == '#':
			blocks.add((x, y))
		elif lab_map[y][x] == '^':
			start = (x, y)

direction = 0

x, y = start
visited = set()
while y < max_y and x < max_x and y >= 0 and x >= 0:
	visited.add((x, y))

	if direction == 0:
		next_pos = (x, y - 1)
	elif direction == 1:
		next_pos = (x + 1, y)
	elif direction == 2:
		next_pos = (x, y + 1)
	else:
		next_pos = (x - 1, y)

	if next_pos in blocks:
		direction = (direction + 1) % 4
		continue

	x, y = next_pos

print(len(visited))

looped = 0

for new_block in visited:
	x, y = start
	direction = 0
	visited = set()
	loop = 1
	while y < max_y and x < max_x and y >= 0 and x >= 0:
		if (x, y, direction) in visited:
			break
		visited.add((x, y, direction))

		if direction == 0:
			next_pos = (x, y - 1)
		elif direction == 1:
			next_pos = (x + 1, y)
		elif direction == 2:
			next_pos = (x, y + 1)
		else:
			next_pos = (x - 1, y)

		if next_pos in blocks or next_pos == new_block:
			direction = (direction + 1) % 4
			continue

		x, y = next_pos
	else:
		loop = 0
	looped += loop

print(looped)