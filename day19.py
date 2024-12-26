import sys
from collections import deque

with open(sys.argv[1]) as f:
   problem = f.read()
   towels, designs = problem.split("\n\n")
   towels = towels.split(", ")
   designs = designs.strip().split("\n")

possible_designs = 0
for design in designs:
   visited = [0] * (len(design) + 1)
   q = deque([0])
   while len(q):
      current_idx = q.popleft()
      if visited[current_idx]:
         continue
      visited[current_idx] = 1
      for towel in towels:
         if towel == design[current_idx:current_idx + len(towel)]:
            q.append(current_idx + len(towel))
   possible_designs += visited[len(design)]

print(possible_designs)

num_arrangements = 0
for design in designs:
   dp = [0] * (len(design) + 1)
   dp[len(design)] = 1
   for current_idx in range(len(design) + 1, -1, -1):
      for towel in towels:
         if towel == design[current_idx:current_idx + len(towel)]:
            dp[current_idx] += dp[current_idx + len(towel)]
   num_arrangements += dp[0]

print(num_arrangements)