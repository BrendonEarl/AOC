import numpy as np
from os import system, name

world = []
maxLength = 0 
iterations = 0

class Cell():
    def __init__(self,up,left,down,right,val) -> None:
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.val = val

    def __repr__(self) -> str:
        return str(self.val)




def possibleDirectionsFromPoint(row, col, val, arr):
    maxRow, maxCol = [num-1 for num in arr.shape]
    directions = []
    canHike = lambda val, check : val >= check or check == val+1


    directions.append(row != 0 and canHike(val,arr[row-1][col]))
    directions.append(col != 0 and canHike(val,arr[row][col-1]))
    directions.append(row != maxRow and canHike(val,arr[row+1][col]))
    directions.append(col != maxCol and canHike(val,arr[row][col+1]))

    return directions


def findSmallestPath(man,goal):
    fsp(man,goal,length = 0,visited=[])
    # print(world)

def fsp(rowCol,goal,length,visited):
    global maxLength, iterations
    iterations += 1
    if not iterations % 1000000:
        system('clear')
        print(f'{iterations} : {length}')
        for row, rowVals in enumerate(world):
            for col, val in enumerate(rowVals):
                if [row,col] in visited:
                    print('-', end= ' ')
                else:
                    print(dig:=chr(val.val), end=' ') 
            print()
        print(f'{visited}-                  -                       -                          -                        -                       -                                -                       -                       - ')
    # print(length)
    if rowCol == goal: 
        maxLength = length if (not maxLength or length<maxLength) else maxLength
        return True
    if maxLength and length > maxLength:
        return False
    if rowCol in visited:
        # print('already visited')
        visited
        return False    
    else:
        test = visited.copy()
        test.append(rowCol)


    row,col = rowCol
    if world[row][col].right:
        fsp([row,col+1],goal,length+1,test)
    if world[row][col].up:
        fsp([row-1,col],goal,length+1,test)
    if world[row][col].down:
        fsp([row+1,col],goal,length+1,test)
    if world[row][col].left:
        fsp([row,col-1],goal,length+1,test)


def main(filename):
    global maxLength
    temp = np.array([[ord(character) for character in line.strip()] for line in open(filename).readlines()],dtype=int)
    shape = temp.shape
    is_edge = lambda row, col, shape: (row in [0,shape[0]-1]) or (col in [0, shape[1]-1])
    man, goal= [0,0], [0,0]

    for row, rowVals in enumerate(temp):
        for col, val in enumerate(rowVals):
            if val in [83,69]: 
                print('T' if val==83 else 'Z',end=' ')
                if val == 83:
                    val = 97
                    man = [row,col]
                    temp[row][col] = ord('a')
                else:
                    val = 122
                    goal = [row,col]
                    temp[row][col] = ord('z')

    for row, rowVals in enumerate(temp):
        rowToAdd = []
        for col, val in enumerate(rowVals):
            if val in [83,69]: 
                print('T' if val==83 else 'Z',end=' ')
                if val == 83:
                    val = 97
                    man = [row,col]
                    temp[row][col] = ord('a')
                else:
                    val = 122
                    goal = [row,col]
                    temp[row][col] = ord('z')

            possible=possibleDirectionsFromPoint(row,col,val,temp)    
            rowToAdd.append(Cell(possible[0],possible[1],possible[2],possible[3],val))
        world.append(rowToAdd.copy())
    # print(temp[20][0])    
        # print()
    # print(world)

    for row in world:
        for val in row:
            print('>' if val.right else '-', end=' ') 
        print()
    print(world[man[0]][man[1]].down)
    print(ord('z'))
    findSmallestPath(man,goal)
    print(maxLength)



main('2022/resources/input_12.txt')