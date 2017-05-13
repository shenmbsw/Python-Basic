# AUTHOR shen shen shs2016f@bu.edu
import sys
import itertools

@profile
def main():
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    d = {}
    for x in f.read().split():
        sx = ''.join(sorted(x))
        l = len(x)
        if l in d.keys():
            try:
                d[l][sx].append(x)
            except:
                d[l][sx] = [x]
        else:
            d[l] = {sx: [x]}
    f.close()

    
    if (1):
        a="randomore 5"
        tag = a.split()
        text = list(tag[0])
        num = int(tag[1])
        result = []
        if num == 0:
            exit(0)
        if num in d.keys():
            k = set(itertools.combinations(sorted(text), num))
            for i in k:
                kw = ''.join((sorted(i)))
                if kw in d[num].keys():
                    for i in d[num][kw]:
                        t = text[:]
                        flag = 1
                        for j in i:
                            try:
                                t.remove(j)
                            except:
                                flag = 0
                        if flag == 1:
                            result.append(i)
        for i in sorted(result):
            print(i)
        print(".")

if __name__=="__main__":
    main()
