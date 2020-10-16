import matplotlib.pyplot as plt
import cv2
from skimage.color import rgb2lab, deltaE_cie76 
import multiprocessing

path = input("Enter the path to the photo: ")
image = cv2.imread(path)

def split(bArr,parts):
    avg = len(bArr) / float(parts)
    out = []
    last = 0.0

    while last < len(bArr):
        out.append(bArr[int(last):int(last + avg)])
        last += avg

    return out


def convert(imgarr):
    dist = [0,0,0,0,0,0,0,0,0]
    for col in imgarr:
        for pix in col: 
            for color in pix:
                dist[int(str(color)[0])-1] += 1
    return dist 

if __name__ == '__main__':
    cores = multiprocessing.cpu_count() 
    batches = split(image, cores) 
    with multiprocessing.Pool(processes=cores) as pool:
        comDist = pool.map(convert, batches)
        finDist = [0,0,0,0,0,0,0,0,0]
        for i in range(len(comDist)): 
            for j in range(len(comDist[i])):
                finDist[j] += comDist[i][j]


tot = sum(finDist) 
for i in range(len(finDist)):
    print(finDist[i]/tot*100)
