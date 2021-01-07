# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:31:49 2020

@author: Nikhil
"""
#sudokuSecondAttempt
import numpy as np
import math
import collections
#TestSudokus
sudoko= np.array([[1,2,3,4],[3,4,2,1],[2,1,4,3],[4,3,1,2]])
easysod=np.array([[0,0,0,3],[0,0,0,2],[3,0,0,0],[4,0,0,0]])
medsod=np.array([[6,5,9,0,1,0,2,8,0],[1,0,0,0,5,0,0,3,0],[2,0,0,8,0,0,0,1,0],[0,0,0,1,3,5,0,7,0],[8,0,0,9,0,0,0,0,2],[0,0,3,0,7,8,6,4,0],[3,0,2,0,0,9,0,0,4],[0,0,0,0,0,1,8,0,0],[0,0,8,7,6,0,0,0,0]])
print(medsod)
hardsod=np.array([[9,5,0,0,0,1,0,0,2],[6,3,0,0,0,0,1,0,0],[0,0,8,0,6,0,0,0,7],[0,0,0,0,0,0,5,0,0],[0,6,1,7,0,9,0,0,0],[0,0,2,0,4,0,0,0,8],[0,9,0,0,0,0,0,0,5],[0,1,0,0,5,6,4,8,0],[0,8,0,0,1,7,0,0,6]])

def possibleRowCol(sod,x,y,gridsize,possibleValues):
        Row = sod[x,:]
        Col = sod[:,y]
        impRow = np.intersect1d(possibleValues,Row)
        impCol = np.intersect1d(possibleValues,Col)     
        impRowCol=np.unique(np.concatenate((impRow,impCol)))
        possible = np.setdiff1d(possibleValues,impRowCol)
        return possible
        
def grid(sod,x,y,gridsize):
	xmin= gridsize*math.floor(x/gridsize)
	xmax=xmin+gridsize
	ymin= gridsize*math.floor(y/gridsize)
	ymax= ymin+gridsize
	grid= sod[xmin:xmax,ymin:ymax]
	return grid,xmin,ymin
	
def possibleGrid(sod,x,y,gridsize,possibleValues):
    Grid = grid(sod,x,y,gridsize)[0]
    impGrid = np.unique(np.intersect1d(possibleValues,np.ravel(Grid)))
    possible = np.setdiff1d(possibleValues,impGrid)
    return possible
	
def possible(sod,x,y,gridsize,possibleValues):
    if sod[x,y]!=0:
        return sod[x,y]
    
    possible=np.intersect1d(possibleRowCol(sod,x,y,gridsize,possibleValues),possibleGrid(sod,x,y,gridsize,possibleValues))
    return possible

def runStep(sod,gridsize):
    possibleValues = np.arange(1,(np.shape(sod)[0])+1)
    xgrid = np.arange(0,gridsize)
    ygrid = np.arange(0,gridsize)
    for i in xgrid:
        for j in ygrid:
            sod=checkgrid(sod,i,j,gridsize,possibleValues)
    return sod

def checkgrid(sod, xgrid, ygrid, gridsize,possibleValues):
    gridPossible = []
    for i in range(gridsize):
        for j in range(gridsize):
            gridPossible.append(np.array(possible(sod,(i+xgrid*gridsize),(j+ygrid*gridsize),gridsize,possibleValues)))
#    print(gridPossible)
    for i in possibleValues:
        OnlyPossible = False
        if sum(i in sublist for sublist in gridPossible)==1:
                OnlyPossible = True
        for subarray in range(len(gridPossible)):
            if (np.size(gridPossible[subarray])==1 or OnlyPossible) and i in gridPossible[subarray]:
#                print(i, subarray)
                x,y = indexToXY(subarray,gridsize)
                sod[x+xgrid*gridsize,y+ygrid*gridsize]=i          
    return sod


def indexToXY(number,gridsize):
    x= math.floor(number/gridsize)
    y= number-gridsize*x
    return x,y
    

def solve(sod):
    gridsize= int(np.sqrt(np.shape(sod)[0]))
    maxcount = gridsize**4
    counter=0
    while (0 in sod and counter<maxcount):
        runStep(sod, gridsize)
        counter +=1
    if 0 in sod:
        return 'Sudoku is unsolvable or has multiple possible solutions'
    return sod

            

#print(grid(medsod, 1,1,3))
possibleValues = np.arange(1,(np.shape(medsod)[0])+1)
#print(possible(medsod,1,1,3,possibleValues))
#possibleValues(easysod,1,1)
#print(runStep(medsod, 3))
#checkgrid(medsod,0,0,3,possibleValues)
#print(checkgrid(medsod,0,0,3,possibleValues))
#print(runStep(medsod, 3))
print(solve(medsod))
print(easysod)
print(solve(easysod))
print(hardsod)
print(solve(hardsod))