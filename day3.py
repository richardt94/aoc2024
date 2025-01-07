from math import prod
import re
import sys

rgx_mul = r"mul\((\d+),(\d+)\)"
rgx_en = r"do\(\)"
rgx_dis = r"don't\(\)"

with open(sys.argv[1]) as f:
    str = f.read()

matches = re.findall(rgx_mul, str)

print(sum([prod([int(g) for g in m]) for m in matches]))

ptr = 0

enabled = True

next_en = re.search(rgx_en, str[ptr:])
next_dis = re.search(rgx_dis, str[ptr:])
next_mul = re.search(rgx_mul, str[ptr:])
lm = next_mul.start()
le = next_en.start()
ld = next_dis.start()

sum = 0

while ptr < len(str):
    if lm < le and lm < ld:
        if enabled:
            sum += int(next_mul.group(1)) * int(next_mul.group(2))
        ptr = lm + 1
        next_mul = re.search(rgx_mul, str[ptr:])
        if next_mul:
            lm = next_mul.start() + ptr
        else: lm = len(str)
    elif ld < le:
        enabled = False
        ptr = ld + 1
        next_dis = re.search(rgx_dis, str[ptr:])
        if next_dis:
            ld = next_dis.start() + ptr
        else: ld = len(str)
    else:
        if not next_en:
            break
        enabled = True
        ptr = le + 1
        next_en = re.search(rgx_en, str[ptr:])
        if next_en:
            le = next_en.start() + ptr
        else: le = len(str)

print(sum)

