# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:31:49 2020

@author: Nikhil
"""
import numpy as np
import math
import collections

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
    for i in possibleValues:
        OnlyPossible = False
        if sum(i in sublist for sublist in gridPossible)==1:
                OnlyPossible = True
        for subarray in range(len(gridPossible)):
            if (np.size(gridPossible[subarray])==1 or OnlyPossible) and i in gridPossible[subarray]:
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

if __name__ == "__main__":
    try:
        input_file = open("input.txt","r")
        sudoku_to_solve = []
        firstline = input_file.readline().strip().split(' ')
        sudoku_to_solve=[firstline]
        for i in range(len(firstline)-1):
            sudoku_to_solve.append(input_file.readline().strip().split(' '))
        sudoku_to_solve = np.array(sudoku_to_solve).astype(int)
        print(solve(np.array(sudoku_to_solve)))
    except:
        print("Input file could not be loaded succesfully")
    finally:
        input_file.close()