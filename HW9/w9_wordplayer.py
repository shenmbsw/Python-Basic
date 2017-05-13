# AUTHOR shen shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu
import sys


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

    while(1):
        tag = input().split()
        text = list(tag[0])
        num = int(tag[1])
        result = []
        if num == 0:
            exit(0)
        elif num == len(text):
            i = d[num][''.join(sorted(text))]
            result = i
        elif num in d.keys():
            for kw in d[num].keys():
                flag = 1
                for j in kw:
                    if j not in text:
                        flag = 0
                        break
                if(flag == 1):
                    try:
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
                    except:
                        continue
        for i in sorted(result):
            print(i)
        print(".")

if __name__ == "__main__":
    main()
