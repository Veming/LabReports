import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
from sklearn import linear_model
import numpy as np
import random

col = ['red', 'blue', 'green', 'cyan', 'magenta', 'yellow', 'black']
__name__ = '__main__'

def initFunc(ptList):
    for i in range(0,30):
        xc=random.uniform(0,20)
        yc=random.uniform(0,20)
        for j in range (0,10):
            xt = random.uniform(xc,xc+3)
            yt = random.uniform(yc,yc+3)
            pt = {'x':xt, 'y':yt}
            ptList.append(pt)
            plt.scatter(xt,yt,color=col[i%7])
    # plt.scatter(x,y,color = 'blue')
    plt.ylabel('Y value')
    plt.xlabel('X value')
    plt.savefig('before.jpg')
    plt.close('all')
    plt.ylabel('Y value')
    plt.xlabel('X value')
    for pt in ptList:
        plt.scatter(pt['x'],pt['y'],color = 'yellow')
        # print(pt['x'],pt['y'])
    plt.savefig('demo.jpg')
    plt.close('all')

def dbscan(ptList, eps, minPts):
    C = 0
    for p in ptList:
        if p.get('Visited') != None:
            continue
        else:
            p['Visited'] = True
            N = getNeighbours(p,ptList,eps)
            if len(N) < minPts:
                p['C'] = -1
            else: 
                C += 1
                expandCluster (p, ptList, N, C, eps, minPts)
    for p in ptList:
        c = p.get('C')
        if c != -1 :
            plt.scatter(p['x'],p['y'],color = col[p.get('C')%7])
        else :
            plt.scatter(p['x'],p['y'],color = 'white')
    plt.ylabel('Y value')
    plt.xlabel('X value')
    plt.savefig('after.jpg')
    plt.close('all')

        
def getNeighbours(p,ptList,eps):
    pts = []
    pts.append(p)
    for q in ptList:
        if pow(p['x']-q['x'],2) + pow(p['y']-q['y'],2) < pow(eps,2):
            pts.append(q)
    return pts

def expandCluster(p, ptList, N, C, eps, minPts):
    p['C'] = C
    for q in N:
        q['Visited'] = True
        n = getNeighbours(q,ptList,eps)
        if len(n) >= minPts:
            for tmpn in n:
                flag = True
                for tmpN in N:
                    if tmpN.get('x') == tmpn.get('x') and tmpN.get('y') == tmpn.get('y'):
                        flag = False
                if flag == True:
                    N.append(tmpn)
        if q.get('C') == None:
            q['C'] = C
                    
def main():
    ptList = []
    initFunc(ptList)
    dbscan(ptList, 2, 2)

if __name__ == '__main__':
    main()