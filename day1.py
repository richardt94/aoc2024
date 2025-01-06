import sys

with open(sys.argv[1]) as f:
   lines = f.readlines()

list1 = []
list2 = []

for line in lines:
   n1, n2 = line.split()
   list1.append(int(n1))
   list2.append(int(n2))

dist = 0
for n1, n2 in zip(sorted(list1), sorted(list2)):
   dist += abs(n1 - n2)

print(dist)

counts = {}

for n2 in list2:
   if n2 in counts:
      counts[n2] += 1
   else:
      counts[n2] = 1


similarity = 0
for n1 in list1:
   if n1 in counts:
      similarity += n1 * counts[n1]

print(similarity)
