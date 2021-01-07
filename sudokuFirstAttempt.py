#sudokuFirstAttempt
#Effective for easy-medium sudokus of n by n format, yet to be tested for n>3
#Does not solve harder sudukos
import numpy as np
#testsudokus
sudoko= np.array([[1,2,3,4],[3,4,2,1],[2,1,4,3],[4,3,1,2]])
easysod=np.array([[0,0,0,3],[0,0,0,2],[3,0,0,0],[4,0,0,0]])
medsod=np.array([[6,5,9,0,1,0,2,8,0],[1,0,0,0,5,0,0,3,0],[2,0,0,8,0,0,0,1,0],[0,0,0,1,3,5,0,7,0],[8,0,0,9,0,0,0,0,2],[0,0,3,0,7,8,6,4,0],[3,0,2,0,0,9,0,0,4],[0,0,0,0,0,1,8,0,0],[0,0,8,7,6,0,0,0,0]])
hardsod=np.array([[9,5,0,0,0,1,0,0,2],[6,3,0,0,0,0,1,0,0],[0,0,8,0,6,0,0,0,7],[0,0,0,0,0,0,5,0,0],[0,6,1,7,0,9,0,0,0],[0,0,2,0,4,0,0,0,8],[0,9,0,0,0,0,0,0,5],[0,1,0,0,5,6,4,8,0],[0,8,0,0,1,7,0,0,6]])

"""for j in easysod:
	for i in j:
		print(i)"""
#intersect removes the zeros
def check(sudoku):
    cols = np.size(sudoku,1)
    rows = np.size(sudoku, 0)
    gridsize=int(np.sqrt(cols))
    for j in range(cols):
        for i in range(rows):
            if sudoku[i,j]==0:
                possibleValues=np.arange(1,cols+1)
                impossiblerowcol=np.union1d(np.intersect1d(possibleValues, sudoku[i,:]),np.intersect1d(possibleValues, sudoku[:,j]))
                impossiblegrid = checkgrid(sudoku,gridsize,i,j)
                impossible = np.unique(np.concatenate((impossiblerowcol, impossiblegrid)))
                if i == 1 & j==0:
                    print(sudoku)
                    print(impossiblegrid)
                possible=np.setdiff1d(possibleValues, impossible)
                if len(possible)==1:
                    sudoku[i,j]=possible[0]
                    return sudoku
					

def checkgrid(sudoku, gridsize, a, b):
    gridID = np.arange(0,gridsize**2)
    gridID = np.reshape(gridID, (gridsize,gridsize))
    gridID = np.kron(gridID, np.ones((gridsize,gridsize)))
    ID = gridID[a,b]
    x,y = np.where(gridID==ID)
    impossiblegrid = []
    for i in range(len(x)):
            if(sudoku[x[i],y[i]]!=0):
                impossiblegrid.append(sudoku[x[i],y[i]])
        
    return np.array(impossiblegrid)



#print(checkgrid(easysod, 2, 3, 1))
#print(np.size(easysod,0))
    

def solve(sod):
    init= np.zeros_like(sod)
    try:
        while 0 in sod:
            init=sod
            sod=check(sod)
        return sod
    except:
        
        return init, 'error'


#print(solve(easysod))
#print(solve(medsod))

print(solve(hardsod)[0])

def advanced(sudoku):
    return 
