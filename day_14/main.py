import numpy as np
from os import system
maxX,minX,maxY = 500,500,0
cave = []

def prnt(array):
    global minX,maxX
    system('clear')
    for i, rowvals in enumerate(array):
        for j, val in enumerate(rowvals[minX-2:]):
            print(val, end=' ')
        print()

def addWalls(instruction):
    global cave
    x, y = 0, 1
    print(instruction)
    for i in range(1,len(instruction)):
        fi, si = instruction[i], instruction[i-1]
        
        if fi[x]==si[x]:
            ex = fi[x]
            if fi[y]<si[y]:
                why = range(fi[y], si[y] +1)
            else:
                why = range(si[y], fi[y] +1)
            print(f'{ex} : {why}')
            for j in why:
                cave[j][ex] = '#'
        elif fi[y]==si[y]:
            why = fi[y]
            if fi[x]<si[x]:
                ex = range(fi[x], si[x] +1)
            else:
                ex = range(si[x], fi[x] +1)
            print(f'{why} : {ex}')
            for j in ex:
                cave[why][j] = '#'
                prnt(cave)

    

def main(filename):
    global maxX,minX,maxY,cave
    wallInstructions = [[[int(index) for index in pair.strip().split(',')] for pair in line.split('->')] for line in open(filename).read().strip().split('\n')]
    [print(instruction) for instruction in wallInstructions]

    maxX,minX,maxY = 500,500,0

    for set in wallInstructions:
        for x,y in set:
            print(f'\t{x},{y}')
            maxX = x if x>maxX else maxX
            minX = x if x<minX else minX
            maxY = y if y>maxY else maxY

    for _ in range(maxY+2):
        new = []
        for _ in range(maxX +2):
            new.append('.')
        cave.append(new)
    
    cave[0][500] = 'x'
    for instruction in wallInstructions:
        addWalls(instruction)
    prnt(cave)

    print(f'\n{minX-1} {maxX+1} : {maxY+1}')
real = 'resources/input_14.txt'
test = 'resources/input_14_test.txt'

main(real)