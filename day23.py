import sys

with open(sys.argv[1]) as f:
   connections = f.readlines()

edges = {}

for connection in connections:
   c1, c2 = connection.strip().split('-')
   if c1 in edges:
      edges[c1].add(c2)
   else:
      edges[c1] = set([c2])
   if c2 in edges:
      edges[c2].add(c1)
   else:
      edges[c2] = set([c1])

sets = set()
for c1 in edges:
   if not c1.startswith('t'):
      continue
   for c2 in edges[c1]:
      for c3 in edges[c2]:
         if c3 in edges[c1]:
            sets.add(tuple(sorted([c1, c2, c3])))

print(len(sets))

V = set(edges.keys())
complement_edges = {}
for c in V:
   complement_edges[c] = V - edges[c]

MIS = set()

for V0 in V:
   this_mis = set([V0])
   to_process = V - this_mis - complement_edges[V0]
   while len(to_process):
      v = tuple(to_process)[0]
      this_mis.add(v)
      to_process.remove(v)
      to_process = to_process - complement_edges[v]
   if len(this_mis) > len(MIS):
      MIS = this_mis
print(",".join(sorted(MIS)))
