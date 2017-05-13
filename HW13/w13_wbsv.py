# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:54:45 2016

@author: shen
"""

from w9_wordplayer import wordplay
from collections import Counter
import json
import numpy as np
#import sys

def isingraph(word,graph):
    print(graph)
    print(word)
    a=np.argwhere(graph == word[0])
    ans = []
    for i in a:
        ans.append(word[0])
        print(i)
        p = []
        p.append(i[0] - 1)
        p.append(i[0] + 2)
        p.append(i[1] - 1)
        p.append(i[1] + 2)
        for j in range(4):
            if p[j] < 0:
                p[j] = 0
            if p[j] > len(graph):
                p[j] = len(graph)
        loc_list = graph[p[0]:p[1],p[2]:p[3]]
        for k in word and k!= word[0]:
            if k in loc_list:
                pass
                
    return [1,ans]


puzz = "puzzles.txt"
f = open(puzz, 'r')
po = []
for x in f.readlines():
    if(x[0])=="{":
        jsondata = x
        po.append(json.loads(jsondata))

print(wordplay("simple_word_list.txt","toscrpsew",5))
for puzzle in po:
    puzzle = po[1]
    leng = puzzle["lengths"]
    size = puzzle["size"]
    grid = (puzzle["grid"])
    b = np.array(list(''.join(grid)), dtype = str).reshape(size,size)

    wordpool = ""
    for i in grid:
        wordpool += i
    ans_pool = []
    first_char = {}
    for i in leng:
        ans_pool.append(wordplay("simple_word_list.txt", wordpool, i))
            
    ans = []
    nth_word={}

    for i in range(len(leng)):
        nth_word[i] = 0
    layer = 0
    print(nth_word)
    while 0<= layer < len(leng):
        flag = 0
        for i in ans_pool[layer][nth_word[layer]:]:
            if isingraph(i,b)[0]:
                ans.append(i)
                nth_word[layer] = ans_pool[layer].index(i) + 1
                layer += 1
                flag = 1
                break
        if flag == 0:
            layer = layer - 1
            if layer >=0:
                print(ans)
                del ans[-1]
            else:
                print ("this list failed")