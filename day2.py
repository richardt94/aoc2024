import sys
with open(sys.argv[1]) as f:
   lines = f.readlines()

n_safe = 0
n_safe_diff = 0
n_safe_rem = 0

for report in lines:
   levels = [int(l) for l in report.split()]
   inc = levels[1] > levels[0]
   if levels[1] == levels[0]:
      inc = levels[2] > levels[1]
   for i in range(1, len(levels)):
      ch = levels[i] if inc else levels[i-1]
      cl = levels[i-1] if inc else levels[i]
      if ch - cl < 1 or ch - cl > 3:
         break
   else:
      n_safe += 1

   diffs = []
   for i in range(1, len(levels)):
      diffs.append(levels[i] - levels[i-1])
   if all([d >= 1 and d <= 3 for d in diffs]):
      n_safe_diff += 1
   elif all([d <= -1 and d >= -3 for d in diffs]):
      n_safe_diff += 1
   
   rem = False
   skipnext = False
   for (i, d) in enumerate(diffs):
      if skipnext:
         skipnext = False
         continue
      if d < 1 or d > 3:
         if rem:
            print("already removed", diffs)
            break
         if i == len(diffs) - 1:
            rem = True
            continue
         if i > 0:
            nd = diffs[i-1] + d
            if nd >= 1 and nd <= 3:
               rem = True
               continue
         if i < len(diffs) - 1:
            nd = diffs[i+1] + d
            if nd >= 1 and nd <= 3:
               rem = True
               skipnext = True
               continue
         if i == 0:
            rem = True
            continue
         print("no removal possible", diffs)
         break

   else:
      n_safe_rem += 1 
      continue
   
   rem = False
   skipnext = False
   diffs = [-d for d in diffs]
   for (i, d) in enumerate(diffs):
      if skipnext:
         skipnext = False
         continue
      if d < 1 or d > 3:
         if rem:
            print("already removed", diffs)
            break
         if i == len(diffs) - 1:
            rem = True
            continue
         if i > 0:
            nd = diffs[i-1] + d
            if nd >= 1 and nd <= 3:
               rem = True
               continue
         if i < len(diffs) - 1:
            nd = diffs[i+1] + d
            if nd >= 1 and nd <= 3:
               rem = True
               skipnext = True
               continue
         if i == 0:
            rem = True
            continue
         print("no removal possible", diffs)
         break

   else:
      n_safe_rem += 1 
      continue
    
            
          
print(n_safe)
print(n_safe_diff)
print(n_safe_rem)
print(len(lines))
