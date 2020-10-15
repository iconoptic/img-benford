import matplotlib.pyplot as plt
import cv2
from skimage.color import rgb2lab, deltaE_cie76 
import multiprocessing

path = input("Enter the path to the photo: ")
image = cv2.imread(path)
dist = [0,0,0,0,0,0,0,0,0]

def convert(pix):
    c = []
    for color in pix:
        c.append(int(str(color)[0])) 
    return c

if __name__ == '__main__':
    p = multiprocessing.Pool() 
    for col in image:
        for i in range(0, len(col), 4): 
            arrs = []
            for j in range(4): 
                if (i+j < len(col)): arrs.append(col[i+j]) 
            out = p.map(convert, arrs)
            for o in out:
                for i in o:
                    dist[i-1] += 1
            out.clear()

tot = sum(dist) 
for i in range(len(dist)):
    print(dist[i]/tot*100)
