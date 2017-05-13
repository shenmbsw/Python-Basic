# AUTHOR Yannan Bai ynbai@bu.edu
# AUTHOR ShenShen shs2016f@bu.edu
from skimage.io import imread
from skimage.transform import rescale
import numpy as np
import json

img_file = []
while True:
    try:
        img_file.append(input())
    except EOFError:
        break
features = {
    'A': [[(28, 1), (0, 14)]],
    'B': [[(18, 24), (27, 9), (15, 12), (17, 6)]],
    'C': [[(24, 26), (0, 12)], [(18, 18)]],
    'D': [[(13, 27), (13, 6)]],
    'E': [[(0, 24), (28, 20)]],
    'F': [[(15, 17), (13, 22), (16, 22)], [(24, 24), (8, 24)]],
    'G': [[(24, 26), (0, 12), (18, 18)]],
    'H': [[(25, 26), (0, 6)]],
    'I': [[(5, 16), (27, 12)], [(25, 6), (0, 5)]],
    'J': [[(5, 16), (27, 12), (25, 6)]],
    'K': [[(13, 15), (28, 27)]],
    'L': [[(28, 24), (0, 12), (8, 12)]],
    'M': [[(27, 0)]],
    'N': [[(28, 26), (10, 8), (16, 19),(15,3)], [(27, 0)]],
    'O': [[(14, 0)], [(29, 18)]],
    'P': [[(0, 20), (6, 25)], [(25, 22)]],
    'Q': [[(29, 22)]],
    'R': [[(8, 25), (28, 20),(13, 11)], [(29, 18)]],
    'S': [[(21, 24), (18, 18), (7, 10), (4, 11)]],
    'T': [[(5, 16), (27, 12), (0, 5)]],
    'U': [[(0, 25), (25, 19), (28, 14)]],
    'V': [[(0, 1)], [(0, 0)]],
    'W': [[(0, 0)]],
    'X': [[(0, 3), (0, 26),(18, 9), (12,1)]],
    'Y': [[(0, 26), (28, 12), (10, 14)]],
    'Z': [[(0, 24), (26, 6), (24, 14), (23, 13)],[(14, 7)]]
    }
for file in img_file:
    image = imread(file, as_grey=True).transpose()
    if image[777][600] < 0.5:
        cnt = 3
        pos_x = 560
        pos_y = 774
        gap = 463
        size = 78
        interval = 170
        black = 4
    elif image[666][580] < 0.5:
        cnt = 4
        pos_x = 503
        pos_y = 717
        gap = 347
        size = 58
        interval = 128
        black = 3
    elif image[600][580] < 0.5:
        cnt = 5
        pos_x = 468
        pos_y = 682
        gap = 278
        size = 47
        interval = 130
        black = 3
    lengths = []
    line1 = [image[:, 2150].transpose()]
    line2 = [image[:, 2150], image[:, 2300]]
    line3 = [image[:, 2080], image[:, 2178], image[:, 2280]]
    if cnt == 3:
        line = line1
    elif cnt == 4:
        line = line2
    else:
    	line = line3
    for row in line:
        count = insec = graph = flag = diff = 0
        for pix in row:
            if pix > 0.49:
                count += 1
                flag = 1
            if flag and pix < 0.5:
                insec += 1
                count = 0
            if count == black:
                graph += 1
                count = 0
                insec = 0
            if insec == interval:
                count = 0
                insec = 0
                if graph:
                    lengths.append(int((graph+1)/2))
                    graph = 0
        if graph:
            lengths.append(int((graph+1)/2))    
    letters = []
    for i in range(cnt):
        for j in range(cnt):
            x = pos_x + gap*j
            y = pos_y + gap*i
            pic = rescale(image[x-size : x+size+1, y-size : y+size+1], 15/size)
            letters.append(pic.transpose())
    puzz = []
    i =  0
    for img in letters:
        for key, feat in features.items():
            flag = True
            feat_in = feat[0]
            for coord in feat_in:
                if img[coord[0]][coord[1]] > 0.75:       
                    flag = False
                    break
            if len(feat) == 2:
                feat_out = feat[1]
                for coord in feat_out:
                    if img[coord[0]][coord[1]] < 0.5:      
                        flag = False
                        break
            if flag:
                puzz.append(key)
                break
    grid = []
    for i in range(cnt):
        word = ''
        for j in range(cnt):
            word += puzz[i + j*cnt]
        grid.append(word)
    result = {}
    result['grid'] = grid
    result['lengths'] = lengths
    result['size'] = cnt
    print(json.dumps(result))
