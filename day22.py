import sys
shifts = [6, -5, 11]
def next(sn):
   for shift in shifts:
      if shift < 0:
         sn = sn ^ (sn >> -shift)
      else:
         sn = (sn ^ (sn << shift)) % (2 ** 24)
   return sn

with open(sys.argv[1]) as f:
   sns = [int(sn) for sn in f.readlines()]

t = 0
for sn in sns:
   for _ in range(2000):
      sn = next(sn)
   t += sn
   
print(t)

deltas = [[] for _ in range(len(sns))]

for _ in range(3):
   for (i, sn) in enumerate(sns):
      nsn = next(sn)
      delta = (nsn % 10 - sn % 10)
      deltas[i].append(delta)
      sns[i] = nsn

sequence_dict = {}

for _ in range(1997):
   for (i, sn) in enumerate(sns):
      nsn = next(sn)
      price = nsn % 10
      delta = (price - sn % 10)
      
      deltas[i].append(delta)
      sns[i] = nsn
      key = tuple(deltas[i][-4:])
      if key in sequence_dict:
         if i not in sequence_dict[key]:
            sequence_dict[key][i] = price
      else:
         sequence_dict[key] = {i : price}

max_price = 0
for key in sequence_dict:
   this_price = sum(sequence_dict[key].values())
   if this_price > max_price:
      max_price = this_price
print(max_price)