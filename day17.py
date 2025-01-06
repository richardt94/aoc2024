import sys
import re

with open(sys.argv[1]) as f:
   data = f.read()
register_matches = re.findall(r"Register ([ABC]): (\d+)", data)
registers = {r[0] : int(r[1]) for r in register_matches}
program_match = re.search(r"Program: ([\d,]+)", data)

program = [int(c) for c in program_match.group(1).split(',')]

print(registers)
print(program)

iA = registers['A']
out_buffer = []
   
A = iA
while A > 0:
   #B = A % 8
   #B = B ^ 1
   #C = A >> B
   #B = B ^ C
   #B = B ^ 4
   B = (A >> ((A % 8) ^ 1)) ^ (A % 8) ^ 5
   A = A >> 3
   
   out_buffer.append(B % 8)

print(out_buffer) 

def output(A):
   return ((A >> ((A % 8) ^ 1)) ^ (A % 8) ^ 5) % 8

def get_valid(A, idx):
   if idx < len(program) and output(A) != program[idx]:
      return False
   else:
      if idx == 0:
         return A
      vm = 8 ** len(program)
      for i in range(8):
         v = get_valid(A * 8 + i, idx - 1)
         if v and v < vm:
            vm = v
      if vm < 8 ** len(program):
         return vm
   return False

v = get_valid(0, len(program))

print(v)

A = v
out_buffer = []
while A > 0:
   #B = A % 8
   #B = B ^ 1
   #C = A >> B
   #B = B ^ C
   #B = B ^ 4
   B = (A >> ((A % 8) ^ 1)) ^ (A % 8) ^ 5
   A = A >> 3
   
   out_buffer.append(B % 8)

print(out_buffer) 

