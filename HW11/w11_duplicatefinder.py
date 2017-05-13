# AUTHOR Shenshen shs2016f@bu.edu
# -*- coding: utf-8 -*-

from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib
import time


def keyget(a):
    match = re.match(r"([a-z]+)([0-9]+)", a, re.I)
    if match:
        items = match.groups()
    return int(items[1])


def cut(a, tblr, i):
    return a[i][tblr[i][0]:tblr[i][1], tblr[i][2]:tblr[i][3]]


def cmp(ac, bc):
    if((ac[:, :] == bc[:, :]).all()):
        return 1
    elif((ac[:, :] == bc[::-1, :]).all()):
        return 1
    elif((ac[:, ::-1] == bc[:, :]).all()):
        return 1
    elif((ac[:, ::-1] == bc[::-1, :]).all()):
        return 1
    else:
        return 0

def main():
    start=time.time()
    file = listdir()
    a = []
    tblr = []
    for i in file:
        if i[-3:] != "png":
            file.remove(i)
    file.sort(key=keyget)
    for i in file:
            tem = imread(i, as_grey=1)
            a.append(tem)
    for i in a:
        par = i.shape[0]
        ver = i.shape[1]
        j = 0
        for j in range(par):
            if i[j].sum() != ver:
                top = j
                break
        for j in range(par-1,-1,-1):
            if i[j].sum() != ver:
                bottom = j + 1
                break
        for j in range(ver):
            if i[:, j].sum() != par:
                left = j
                break
        for j in range(ver-1,-1,-1):
            if i[:, j].sum() != par:
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
                    if (np.equal(ac.sum(), bc.sum()) == "False"):
                        flag = 0
                    elif (ac.shape == bc.shape):
                        if (ac.shape[0] != ac.shape[1]):
                            flag = cmp(ac, bc)
                        else:
                            flag = cmp(ac, bc)
                            if (flag == 0):
                                ac = ac.swapaxes(0, 1)
                                flag = cmp(ac, bc)
                    elif ((ac.shape[1], ac.shape[0]) == bc.shape[0:2]):
                        ac = ac.swapaxes(0, 1)
                        flag = cmp(ac, bc)
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
    with open("answers.txt", "w") as f:
        f.write(string)
    sha = hashlib.sha256(string.encode())
    print(sha.hexdigest())
    print(time.time()-start)
if __name__ == "__main__":
    main()

