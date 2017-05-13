# -*- coding: utf-8 -*-


import sys
import itertools

file_name = sys.argv[1]
f = open(file_name, 'r')
md = {}
for line in f:
    l = line.strip('\n')
    key = l[0]+str(len(l))
    if key in md.keys():
        md[key].append(l)
    else:
        md[key] = [l]
f.close


while 1:

    tag = input().split()
    text = tag[0]
    num = int(tag[1])
    c = []
    output = []
    if (num == 0):
        exit(0)
    else:
        k = set(itertools.permutations(text, num))
        for i in k:
            c.append(''.join(i))
        word = set(text)
        for i in word:
            ke = i+str(num)
            if ke in md.keys():
                for j in md[ke]:
                    if j in c:
                        output.append(j)

    for x in sorted(output):
        print(x)
    print(".")
