import sys

file_name = sys.argv[1]
f = open(file_name, 'r')
d = {}
for x in f.read().split():
    if len(x) in d.keys():
        d[len(x)].append(x)
    else:
        d[len(x)] = [x]
f.close()

while(1):
    tag = input().split()
    text = list(tag[0])
    num = int(tag[1])
    if num == 0:
        exit(0)
    if num in d.keys():
        word = d.get(num)
        result = []
        for w in word:
            flag = 1
            wl = list(w)
            t = text
            for i in wl:
                if i not in text:
                    flag == 0
                else:
                    text.remove(i)
            if flag == 1:
                result.append(w)
        for i in sorted(result):
            print(i)
    print('.')
