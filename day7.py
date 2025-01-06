import sys

with open(sys.argv[1]) as f:
   eqns = f.readlines()

total = 0
for eqn in eqns:
   test, vals = eqn.split(':')
   test = int(test)
   vals = [int(v) for v in vals.strip().split(' ')]
   possible = [vals[0]]
   for v in vals[1:]:
      np = []
      for pv in possible:
         np.append(pv + v)
         np.append(pv * v)
         np.append(int(str(pv) + str(v)))
      possible = np
   if test in possible:
      #print("yes")
      total += test
   #else: print("no")

print(total)
