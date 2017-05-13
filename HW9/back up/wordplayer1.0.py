# AUTHOR shen shen shs2016f@bu.edu
import sys

file_name = sys.argv[1]
f = open(file_name, 'r')
d = {}
for x in f.read().split():
    sx = ''.join(set(x))
    if len(x) in d.keys():
        if sx in d[len(x)].keys():
            d[len(x)][sx].append(x)
        else:
            d[len(x)][sx] = [x]
    else:
        d[len(x)] = {sx: [x]}

f.close()

while(1):
    tag = input().split()
    text = tag[0]
    num = int(tag[1])
    result = []
    if num == 0:
        exit(0)
    if num in d.keys():
        for fl in d[num].keys():
            if set(fl).issubset(set(text)):
                for word in d[num][fl]:
                    flag = 1
                    t = list(text)
                    for i in word:
                        try:
                            t.remove(i)

                        except:
                            flag = 0
                    if (flag == 1):
                        result.append(word)

    for i in sorted(result):
        print(i)
    print('.')

