from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib


def keyget(a):
    match = re.match(r"([a-z]+)([0-9]+)", a, re.I)
    if match:
        items = match.groups()
    return int(items[1])


def cut(a, tblr, i):
    return a[i][tblr[i][0]:tblr[i][1], tblr[i][2]:tblr[i][3]]


def main():
    file = listdir()
    a = []
    tblr = []
    for i in file:
        if i[-3:] != "png":
            file.remove(i)
    file.sort(key = keyget)
    for i in file:
        tem = imread(i,as_grey=1)
        a.append(tem)
    
    for i in a:
        par = i.shape[0]
        ver = i.shape[1]
        j = 0
        while (j < par):
            if i[j].sum() == ver:
                j += 1
            else:
                top = j
                break
        j = par - 1
        while (j > 0):
            if i[j].sum() == ver:
                j = j - 1
            else:
                bottom = j + 1
                break
        j = 0
        while (j < ver):
            if i[:, j].sum() == par:
                j += 1
            else:
                left = j
                break
        j = ver - 1
        while (j > 0):
            if i[:, j].sum() == par:
                j = j - 1
            else:
                right = j+1
                break
        tblr.append((top, bottom, left, right))

    b = len(a)
    result = []
    used = []
    count = 0
    for i in range(b):
        if i not in used:
            result.append([file[i]])
            for j in range(i+1, b):
                if j not in used:
                    flag = 1
                    ac = cut(a, tblr, i)
                    bc = cut(a, tblr, j)
                    if (np.equal(ac.sum(),bc.sum())=="False"):
                        flag = 0
                    if flag == 1:
                        bd1 = []
                        bd2 = []
                        if ((ac.shape == bc.shape) or ((ac.shape[1], ac.shape[0]) == bc.shape[0:2])):
                            bd1.append(ac[1])
                            bd1.append(ac[1:ac.shape[0]-1, ac.shape[1]-1])
                            bd1.append(ac[ac.shape[0]-1, 0:ac.shape[0]:-1])
                            bd1.append(ac[1:ac.shape[0]-2, 0])
                            bd2.append(bc[1])
                            bd2.append(bc[1:bc.shape[0]-1, bc.shape[1]-1])
                            bd2.append(bc[bc.shape[0]-1, 0:bc.shape[0]:-1])
                            bd2.append(bc[1:bc.shape[0]-2:-1, 0])

                            m1 = 1
                            for k in bd1:
                                for l in k:
                                    m1 = m1*l
                            m2 = 1
                            for k in bd2:
                                for l in k:
                                    m2 = m2*l
                            if(m1 == m2):
                                pass
                        else:
                            flag = 0
                    if flag == 1:
                        result[count].append(file[j])
                        used.append(j)
            count += 1

    string = ""
    for i in result:
        string += ' '.join(i)
        string += '\n'
    print(string)
    sha = hashlib.sha256(string.encode())
    print(sha.hexdigest())

if __name__ == "__main__":
    main()
