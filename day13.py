import sys, re

from math import gcd

problem_rgx = r"""Button A: X\+(\d+), Y\+(\d+)
Button B: X\+(\d+), Y\+(\d+)
Prize: X=(\d+), Y=(\d+)"""

with open(sys.argv[1]) as f:
   data = f.read()
total_cost = 0
for m in re.findall(problem_rgx, data):
   xA, yA = int(m[0]), int(m[1])
   xB, yB = int(m[2]), int(m[3])
   xT, yT = int(m[4]), int(m[5])

   maxB = min(yT // yB, xT // xB, 100)

   min_cost = 0
   for nB in range(maxB, 0, -1):
      nA = (yT - yB * nB) // yA
      if (nA * xA + nB * xB, nA * yA + nB * yB) == (xT, yT) and nA <= 100:
         min_cost = 3 * nA + nB
         total_cost += min_cost
         break

print(total_cost)

total_cost = 0
for m in re.findall(problem_rgx, data):
   xA, yA = int(m[0]), int(m[1])
   xB, yB = int(m[2]), int(m[3])
   xT, yT = 10000000000000 + int(m[4]), 10000000000000 + int(m[5])
   # xT, yT = int(m[4]), int(m[5])

   maxB = min(yT // yB, xT // xB)

   # find min nA, max nB s.t. xT == nB * xB + nA * xA
   for nB in range(maxB, maxB - xA, -1):
      if (xT - xB * nB) % xA == 0:
         break
   else: 
      continue
   
   # increase nA in steps such that the remainder is divisible by xB.
   # checking for a point where yT = mB * yB + nA * yA.
   # mB is not necessarily equal to nB.
   # because arithmetic here is % yB, if we don't find a solution within yB steps 
   # there will be no solution
   dx = xA * xB // gcd(xA, xB)
   dA = dx // xA
   dB = dx // xB
   nA = (xT - xB * nB) // xA
   for _ in range(min(yB, nB // dB + 1)):
      if (yT - yA * nA) % yB == 0:
         break
      nA += dA
      nB -= dB
   else:
      continue

   mB = (yT - nA * yA) // yB
   # do some maths to find the solution
   dA_y = yB // gcd(yA, yB)
   dA = dA * dA_y // gcd(dA, dA_y)
   dB_x = dA * xA // xB
   dB_y = dA * yA // yB

   if nB != mB:
      # print(dB_x, dB_y, nB, mB, 'mis')
      if (nB - mB) % (dB_x - dB_y):
         continue
      steps = (mB - nB) // (dB_x - dB_y)
      nA -= steps * dA
      nB += dB_x * steps
      mB += dB_y * steps
      
   # print(nA, nB, xA * nA + xB * nB, yA * nA + yB * nB)
   total_cost += 3 * nA + nB

      
print(total_cost)
