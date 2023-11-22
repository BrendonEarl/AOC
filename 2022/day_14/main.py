import numpy as np
from os import system
maxX,minX,maxY = 500,500,0
cave = []

def prnt(array, min=0):
    global minX,maxX
    system('clear')
    for i, rowvals in enumerate(array[min:]):
        for j, val in enumerate(rowvals[minX-2:maxX +5]):
            print(val, end=' ')
        print()

def addWalls(instruction):
    global cave
    x, y = 0, 1
    for i in range(1,len(instruction)):
        fi, si = instruction[i], instruction[i-1]
        
        if fi[x]==si[x]:
            ex = fi[x]
            if fi[y]<si[y]:
                why = range(fi[y], si[y] +1)
            else:
                why = range(si[y], fi[y] +1)
            for j in why:
                cave[j][ex] = '#'
        elif fi[y]==si[y]:
            why = fi[y]
            if fi[x]<si[x]:
                ex = range(fi[x], si[x] +1)
            else:
                ex = range(si[x], fi[x] +1)
            for j in ex:
                cave[why][j] = '#'

def playgame(cave, part1=False):
    isWallOrSand = lambda y, x : cave[y][x] == '#' or cave[y][x] == 'o'
    grains = 0
    break_flag = False

    while True:
        if break_flag: return grains -1 if part1 else grains
        grains += 1
        grainy,grainx = 0,500
        while True:
            if part1:
                if grainy + 1 > maxY:
                    break_flag = True
                    break
            if isWallOrSand(grainy+1,grainx):
                if isWallOrSand(grainy+1,grainx-1):
                    if isWallOrSand(grainy+1,grainx+1):
                        cave[grainy][grainx] = 'o'
                        if grainy == 0 and grainx == 500:
                            break_flag = True
                        if grains % 20 == 0:
                            prnt(cave)
                        break
                    else:
                        grainy += 1
                        grainx +=1
                else:
                    grainy += 1
                    grainx -= 1
            else:
                grainy += 1


def main(filename, part1=False):
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
        for _ in range(maxX * 2):
            new.append('.')
        cave.append(new)
    
    cave[0][500] = 'x'
    for instruction in wallInstructions:
        addWalls(instruction)
    if not part1:
        floor = []
        for i in range(maxX*2):
            floor.append('#')
        cave.append(floor)

    print(playgame(cave,part1))

real = 'resources/input_14.txt'
test = 'resources/input_14_test.txt'


main(real)