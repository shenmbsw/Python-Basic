# AUTHOR shen shen shs2016f@bu.edu
# AUTHOR You Han yhan94@bu.edu


def wordplay(file_name, tag1, tag2):
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

    text = list(tag1)
    num = tag2
    result = []
    if num == 0:
        exit(0)
    elif num == len(text):
        sort_text = ''.join(sorted(text))
        if sort_text in d[num]:
            result = d[num][sort_text]
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
    return (result)