# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:37:40 2016

@author: shen
"""
from w9_wordplayer import wordplay
from collections import Counter
import json
import numpy as np








if __name__ == "__main__":

    puzzle = []
    while True:
        js = input("")    
        try:     
            puzzle.append(json.loads(js))
        except:
            break

    for puz in range(len(all_puzzles)):
        answer = ans("simple_word_list.txt")

        if (len(answer) == 0):
            answer =ans("large_word_list.txt")

        for i in answer:
            for j in i:
                print(j, end=" ")
            print("")
print(".")