# -*- coding: utf-8 -*-


import sys
import itertools
import time

file_name = sys.argv[1]
f = open(file_name, 'r')
md = {}
st=time.time()
for line in f:
    l = line.strip('\n')
    key = len(l)
    if key in md.keys():
        md[key].append(l)
    else:
        md[key] = [l]
f.close

print("creat:",time.time()-st)


while 1:

    tag = input().split()
    text = tag[0]
    num = int(tag[1])
    output = []
    if (num == 0):
        exit(0)
    else:
        st=time.time()
        k = set(itertools.permutations(text, num))
        per=time.time()
        for i in k:
            a = ''.join(i)
            try:
                if a in md[num]:
                    output.append(a)
            except:
                continue
    sort=time.time()
    for x in sorted(output):
        print(x)
    print(".")
    print("arrange",per-st)
    print("search",sort-per)
    print("sort",time.time()-sort)