# AUTHOR ShenShen shs2016f@bu.edu
# AUTHOR YouHan yhan94@bu.edu

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


def cmp(ac, bc):
    if((np.all(ac == bc)) or
       (np.all(ac == bc[::-1, :])) or
       (np.all(ac[:, ::-1] == bc)) or
       (np.all(ac[:, ::-1] == bc[::-1, :]))):
        return 1
    else:
        return 0


def main():
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
        i = i - 1
        oz = i.nonzero()
        tblr.append((np.amin(oz[0]),
                     np.amax(oz[0]) + 1,
                     np.amin(oz[1]),
                     np.amax(oz[1]) + 1))

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
                    if flag == 1:
                        if (ac.shape == bc.shape or
                           (ac.shape[1], ac.shape[0]) == bc.shape[0:2]):
                            flag = cmp(ac, bc)
                            if (flag == 0):
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

if __name__ == "__main__":
    main()
