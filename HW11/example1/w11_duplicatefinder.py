# -*- coding: utf-8 -*-

from os import listdir
import re
from skimage.io import imread
import numpy as np
import hashlib


def keyget(a):
    if(a[-6].isdigit()):
        return int(a[-6:-4])
    else:
        return int(a[-5])


def cut(a, tblr, i):
    return a[i][tblr[i][0]:tblr[i][1], tblr[i][2]:tblr[i][3], :]


def cmp(a,b):
    return 1


def main():
#read form sorted file 
    file = listdir()
    a = []
    tblr = []
    for i in file:
        if i[-3:] != "png":
            file.remove(i)
    file.sort(key=keyget)
    for i in file:
            tem = imread(i)
            tem[tem==0]=1
            tem[tem==255]=0
            a.append(tem)
#find not blank area
    for i in a:
        par = i.shape[0]
        ver = i.shape[1]
        j = 0
        while (j < par):
            if i[j].sum() == 0:
                j += 1
            else:
                top = j
                break
        j = par - 1
        while (j > 0):
            if i[j].sum() == 0:
                j = j - 1
            else:
                bottom = j + 1
                break
        j = 0
        while (j < ver):
            if i[:, j].sum() == 0:
                j += 1
            else:
                left = j
                break
        j = par - 1
        while (j > 0):
            if i[:, j].sum() == 0:
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
                flag = 1
                ac=cut(a, tblr, i)
                bc=cut(a, tblr, j)
                for rbg in range(3):
                    if (ac[:, :, rbg].sum() != bc[:, :, rbg].sum()):#1st compare through the sum of each color
                        flag = 0
                        break
                if flag == 1:
                    for rgb in range(3):#2nd compare through the line
                        pass
                if flag == 1:    
                    result[count].append(file[j])
                    used.append(j)
            count += 1

    print(result)

if __name__ == "__main__":
    main()
