import sys

class Wire:
   def __init__(self, parents=None, value=None, operation=None):
      self.val = value
      self.parents = parents
      self.operation = operation

   @property  
   def value(self):
      if self.val is None:
         v1 = self.parents[0].value
         v2 = self.parents[1].value
         # print(self.operation)
         if self.operation == 'AND':
            self.val = v1 and v2
         if self.operation == 'OR':
            self.val = v1 or v2
         if self.operation == 'XOR':
            self.val = v1 ^ v2
      return self.val


wires = {}

with open(sys.argv[1]) as f:
   data = f.read().strip()

literals, operations = data.split("\n\n")

for literal in literals.split("\n"):
   name, value = literal.split(":")
   wires[name] = Wire(value=int(value) != 0)

for operation in operations.split("\n"):
   op, destination = operation.split("->")
   p1, optype, p2 = [word.strip() for word in op.split()]
   if p1 not in wires:
      par1 = Wire()
      wires[p1] = par1
   else:
      par1 = wires[p1]
   if p2 not in wires:
      par2 = Wire()
      wires[p2] = par2
   else:
      par2 = wires[p2]
   if destination.strip() in wires:
      dst = wires[destination.strip()]
      dst.parents = (par1, par2)
      dst.operation = optype
   else:
      wires[destination.strip()] = Wire(parents=(par1, par2), operation=optype)

total = 0
total_x = 0
total_y = 0
for k in sorted(wires.keys()):
   if k.startswith('z'):
      total += int(wires[k].value) * 2 ** int(k[1:])
   elif k.startswith('y'):
      total_y += int(wires[k].value) * 2 ** int(k[1:])
   elif k.startswith('x'):
      total_x += int(wires[k].value) * 2 ** int(k[1:])

print(total_x, total_y)
print(f"{total:b}")
print(f"{total_x + total_y:b}")

for bit in range(45):
   print(f"bit: {bit:02d}")
   axorb = "000"
   aandb = "000"
   for operation in operations.split("\n"):
      op, destination = operation.split("->")
      p1, optype, p2 = [word.strip() for word in op.split()]
      if f"x{bit:02d}" in [p1, p2] and f"y{bit:02d}" in [p1, p2]:
         if optype == "XOR":
            axorb = destination.strip()
         if optype == "AND":
            aandb = destination.strip()

   print(f"A^B: {axorb}")
   print(f"A&B: {aandb}")
   cin = "000"
   cin2 = "000"
   sout = "000"
   cint = "000"
   for operation in operations.split("\n"):
      op, destination = operation.split("->")
      p1, optype, p2 = [word.strip() for word in op.split()]
      if axorb in [p1, p2]:
         if optype == "XOR":
            if p1 == axorb:
               cin = p2
            else:
               cin = p1
            sout = destination.strip()
         if optype == "AND":
            if p1 == axorb:
               cin2 = p2
            else:
               cin2 = p1
            cint = destination.strip()
   print(f"Cin(sum): {cin}")
   print(f"Cin(Cout): {cin2}")
   print(f"Cin&(A^B): {cint}")
   print(f"sum: {sout}")

   cout = "000"
   for operation in operations.split("\n"):
      op, destination = operation.split("->")
      p1, optype, p2 = [word.strip() for word in op.split()]
      if cint in [p1, p2] and aandb in [p1, p2] and optype == "OR":
         cout = destination.strip()

   print(f"Cout: {cout}")
   print()

