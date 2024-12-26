import sys
from collections import deque

with open(sys.argv[1]) as f:
   buf_targets = [c.strip() for c in f.readlines()]

moves_numpad = {
   ('0', '^') : '2',
   ('0', '>') : 'A',
   ('1', '>') : '2',
   ('1', '^') : '4',
   ('2', 'v') : '0',
   ('2', '<') : '1',
   ('2', '>') : '3',
   ('2', '^') : '5',
   ('3', 'v') : 'A',
   ('3', '<') : '2',
   ('3', '^') : '6',
   ('4', '>') : '5',
   ('4', 'v') : '1',
   ('4', '^') : '7',
   ('5', 'v') : '2',
   ('5', '^') : '8',
   ('5', '<') : '4',
   ('5', '>') : '6',
   ('6', '<') : '5',
   ('6', '^') : '9',
   ('6', 'v') : '3',
   ('7', 'v') : '4',
   ('7', '>') : '8',
   ('8', '<') : '7',
   ('8', '>') : '9',
   ('8', 'v') : '5',
   ('9', '<') : '8',
   ('9', 'v') : '6',
   ('A', '^') : '3',
   ('A', '<') : '0',
}

moves_dirpad = {
   ('<', '>') : 'v',
   ('v', '^') : '^',
   ('v', '<') : '<',
   ('v', '>') : '>',
   ('^', 'v') : 'v',
   ('^', '>') : 'A',
   ('>', '<') : 'v',
   ('>', '^') : 'A',
   ('A', 'v') : '>',
   ('A', '<') : '^',
}

def push_a(state):
   test_idx = len(state) - 1
   while state[test_idx] == 'A' and test_idx > 0:
      test_idx -= 1
   if test_idx == 0:
      return state
   else:
      direction = state[test_idx]
      if test_idx == 1:
         if (state[0], direction) not in moves_numpad: return state
         new_state_code = moves_numpad[(state[0], direction)]
      else:
         if (state[test_idx - 1], direction) not in moves_dirpad: return state
         new_state_code = moves_dirpad[(state[test_idx - 1], direction)]
      return state[:test_idx - 1] + new_state_code + state[test_idx:]

complexity = 0
for buf_target in buf_targets:
   initial_state = "AAA"
   total_length = 0
   for (i, ch) in enumerate(buf_target):
      state_target = ch + "AA"
      visited = set()
      q = deque([(0, initial_state)])

      while len(q):
         length, state = q.popleft()
         if state in visited:
            continue
         if state == state_target:
            break
         for direction in ['<', '^', '>', 'v']:
            if (state[-1], direction) in moves_dirpad:
               q.append((length + 1, state[:-1] + moves_dirpad[(state[-1], direction)]))


         result = push_a(state)
         if result != state:
            q.append((length + 1, result))

         visited.add(state)
      total_length += length + 1
      print(length)
      initial_state = state_target
   print(total_length)
   print()
   complexity += total_length * int(buf_target[:-1])

print(complexity)



# complexity = 0
# for buf_target in buf_targets:
#    initial_state = "A" * 6
#    total_length = 0
#    for (i, ch) in enumerate(buf_target):
#       state_target = ch + "A" * 5
#       visited = set()
#       q = deque([(0, initial_state)])

#       while len(q):
#          length, state = q.popleft()
#          # print(length)
#          if state in visited:
#             continue
#          if state == state_target:
#             break
#          for direction in ['<', '^', '>', 'v']:
#             if (state[-1], direction) in moves_dirpad:
#                q.append((length + 1, state[:-1] + moves_dirpad[(state[-1], direction)]))


#          result = push_a(state)
#          if result != state:
#             q.append((length + 1, result))

#          visited.add(state)
#       total_length += length + 1
#       initial_state = state_target
#    print(total_length)
#    complexity += total_length * int(buf_target[:-1])

# print(complexity)

numpad_locs = {
   '7' : (0, 0),
   '8' : (1, 0),
   '9' : (2, 0),
   '4' : (0, 1),
   '5' : (1, 1),
   '6' : (2, 1),
   '1' : (0, 2),
   '2' : (1, 2),
   '3' : (2, 2),
   '0' : (1, 3),
   'A' : (2, 3),
}

dpad_paths = {
   ('A', '<') : ['v<<'],
   ('A', '^') : ['<'],
   ('A', '>') : ['v'],
   ('A', 'v') : ['v<', '<v'],
   ('<', 'A') : ['>>^'],
   ('<', '^') : ['>^'],
   ('<', 'v') : ['>'],
   ('<', '>') : ['>>'],
   ('^', 'A') : ['>'],
   ('^', '<') : ['v<'],
   ('^', 'v') : ['v'],
   ('^', '>') : ['>v', 'v>'],
   ('>', 'A') : ['^'],
   ('>', '^') : ['<^', '^<'],
   ('>', '<') : ['<<'],
   ('>', 'v') : ['<'],
   ('v', 'A') : ['^>', '>^'],
   ('v', '<') : ['<'],
   ('v', '>') : ['>'],
   ('v', '^') : ['^'],
}

dp = {}

def expand_dpad(lA, lB, n):
   if (lA, lB, n) in dp:
      return dp[(lA, lB, n)]
   if lA == lB:
      dp[(lA, lB, n)] = 0
      return 0
   if n == 0:
      dp[(lA, lB, n)] = 0
      return 0

   dists = []
   for path in dpad_paths[(lA, lB)]:
      d = len(path)
      lAn = 'A'
      for lBn in path:
         d += expand_dpad(lAn, lBn, n - 1)
         lAn = lBn
      d += expand_dpad(lAn, 'A', n - 1)
      dists.append(d)
   mind = min(dists)
   dp[(lA, lB, n)] = mind
   return mind

def expand_numpad(lA, lB, n):
   if lA == lB:
      return 0
   if n == 0:
      return 0
   loc_A = numpad_locs[lA]
   loc_B = numpad_locs[lB]
   dx = loc_B[0] - loc_A[0]
   dy = loc_B[1] - loc_A[1]
   hdist = abs(dx) + abs(dy)

   if dx == 0: 
      yC = '^' if dy < 0 else 'v'
      return hdist + expand_dpad('A', yC, n - 1) + expand_dpad(yC, 'A', n - 1)
   if dy == 0: 
      xC = '<' if dx < 0 else '>'
      return hdist + expand_dpad('A', xC, n - 1) + expand_dpad(xC, 'A', n - 1)

   if loc_B[0] == 0 and loc_A[1] == 3:
      return hdist + expand_dpad('A', '^', n - 1) + expand_dpad('^', '<', n - 1) + expand_dpad('<', 'A', n - 1)
   if loc_B[1] == 3 and loc_A[0] == 0:
      return hdist + expand_dpad('A', '>', n - 1) + expand_dpad('>', 'v', n - 1) + expand_dpad('v', 'A', n - 1)
   if dx > 0:
      xC = '>'
   else:
      xC = '<'
   if dy > 0:
      yC = 'v'
   else:
      yC = '^'
   d1 = expand_dpad('A', xC, n - 1) + expand_dpad(xC, yC, n - 1) + expand_dpad(yC, 'A', n - 1)
   d2 = expand_dpad('A', yC, n - 1) + expand_dpad(yC, xC, n - 1) + expand_dpad(xC, 'A', n - 1)
   return min(d1, d2) + hdist

print()

n_exp = 26

complexity = 0
for buf_target in buf_targets:
   lA = 'A'
   d = len(buf_target)
   for lB in buf_target:
      dd = expand_numpad(lA, lB, n_exp)
      print(dd)
      d += dd#expand_numpad(lA, lB, n_exp)
      lA = lB
   complexity += d * int(buf_target[:-1])
   print("=", d)
   print()

print(complexity)

# path = ">^"

# lA = 'A'
# d = len(path)
# for lB in path:
#    dn = expand_dpad(lA, lB, 2)
#    print(dn)
#    d += dn
#    lA = lB
# print(d)