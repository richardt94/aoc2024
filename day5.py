from copy import deepcopy
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

rules = {}
rules_inv = {}

for (i, line) in enumerate(lines):
    rule = line.split('|')
    if len(rule) < 2:
        break
    
    first = int(rule[0])
    second = int(rule[1])
    if first in rules:
        rules[first].add(second)
    else:
        rules[first] = set([second])

    if second in rules_inv:
        rules_inv[second].add(first)
    else:
        rules_inv[second] = set([first])

total = 0

invalid_updates = []
for update in lines[i + 1:]:
    seen = set()
    valid = False
    for page in update.split(','):
        p = int(page)
        if p in rules:
            broken = True
            for second in rules[p]:
                if second in seen:
                    invalid_updates.append(update)
                    break
            else:
                broken = False
            if broken:
                break
        seen.add(int(page))
    else:
        valid = True
    if valid:
        ulen = len(update.split(','))
        total += int(update.split(',')[ulen // 2])

print(total)

total_fixed = 0
for ustr in invalid_updates:
    update = set([int(page) for page in ustr.split(',')])
    sorted_pages = []
    ri = deepcopy(rules_inv)
    for page in list(ri.keys()):
        if page not in update:
            del ri[page]
            continue
        for page2 in list(ri[page]):
            if page2 not in update:
                ri[page].remove(page2)
                if not len(ri[page]):
                    del ri[page]

    while len(update):
        for page in list(update):
            if page not in ri:
                sorted_pages.append(page)
                update.remove(page)
                for page2 in list(ri.keys()):
                    ri[page2].remove(page)
                    if not len(ri[page2]):
                        del ri[page2]

    total_fixed += sorted_pages[len(sorted_pages) // 2]

print(total_fixed)
