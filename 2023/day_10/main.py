import numpy as np
from math import floor
import sys
from time import sleep
np.set_printoptions(threshold=sys.maxsize)

class Cell:
    LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3

    def __init__(self, v) -> None:
        self.v = v
        self.l, self.u, self.r, self.d = None, None, None, None
        self.connections = []

    def setNeighbors(self, l: "Cell", u: "Cell", r: "Cell", d: "Cell"):
        self.l, self.u, self.r, self.d = l, u, r, d
        self.setConnections()

    def setConnections(self):
        up = ["|", "7", "F", "S"]
        down = ["L", "J", "|", "S"]
        left = ["L", "F", "-", "S"]
        right = ["-", "J", "7", "S"]

        match self.v:
            case "|":
                if (self.u and self.d) and ((self.u.v in up) and (self.d.v in down)):
                    self.connections = [self.u, self.d]
            case "-":
                if (self.l and self.r) and ((self.l.v in left) and (self.r.v in right)):
                    self.connections = [self.l, self.r]
            case "7":
                if (self.l and self.d) and ((self.l.v in left) and (self.d.v in down)):
                    self.connections = [self.l, self.d]
            case "F":
                if (self.r and self.d) and ((self.r.v in right) and (self.d.v in down)):
                    self.connections = [self.r, self.d]
            case "J":
                if (self.u and self.l) and ((self.u.v in up) and (self.l.v in left)):
                    self.connections = [self.u, self.l]
            case "L":
                if (self.u and self.r) and ((self.u.v in up) and (self.r.v in right)):
                    self.connections = [self.u, self.r]
            case "S":
                if self.u and self.u.v in up:
                    self.connections.append(self.u)
                if self.d and self.d.v in down:
                    self.connections.append(self.d)
                if self.l and self.l.v in left:
                    self.connections.append(self.l)
                if self.r and self.r.v in right:
                    self.connections.append(self.r)
            case _:
                pass
    def get(self,s):
        match s:
            case 'l':
                return self.l
            case 'u':
                return self.u
            case 'r':
                return self.r
            case 'd':
                return self.d
    
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.v


def main(fn, pt1=True):
    with open(fn) as f:
        lines = [[*line.strip()] for line in f]
    f.close

    maze = np.array(lines, dtype=object)
    # print(maze)

    mrow, mcol = [m - 1 for m in maze.shape]

    for i, line in enumerate(maze):
        for j, ch in enumerate(line):
            if ch == "S":
                start = [i, j]
            maze[i][j] = Cell(ch)

    for i, line in enumerate(maze):
        for j, ch in enumerate(line):
            l, u, r, d = None, None, None, None
            if i > 0:
                u = maze[i - 1][j]
            if i < mrow:
                d = maze[i + 1][j]
            if j > 0:
                l = line[j - 1]
            if j < mcol:
                r = line[j + 1]

            maze[i][j].setNeighbors(l, u, r, d)

    startr, startc = start

    print(maze)

    for i, line in enumerate(maze):
        for j, ch in enumerate(line):
            if not maze[i][j].connections:
                maze[i][j].v = '.'
    
    s = maze[startr][startc]
    check = s.connections[0]
    used = [s,check]
    while check.v != 'S':
        print(f'{check} conn: {check.connections} - {check.connections[0] in used} {check.connections[1] in used}')
        
        
        if all([c in used for c in check.connections]):
            break
        nxt = check.connections[0] if check.connections[0] not in used else check.connections[1]
        check = nxt
        used.append(nxt)
    

    # print(maze)
    print(s)
    print(int(floor(len(used))/2))

    for line in maze:
        for ch in line:
            if ch not in used:
                ch.v = '.'
            else:
                ch.v = '0'
            print(ch,end='')
        print()
    

    direction = ''
    g,b = 0,2
    t = ['l', 'u', 'r', 'd']
    x = {
        'l' : -1,
        'r' : 1
    }
    p = {
            'u' : {
                'l': 'l',
                'r': 'r'
            },
            'd' : {
                'l' : 'r',
                'r' : 'l',
            },
            'l' : {
                'u' : 'r',
                'd' : 'l',
            },
            'r' : {
                'u' : 'l',
                'd' : 'r'
            },
        }
    y = {
        -1 : 3,
        4 : 0
    }
    for i, u in enumerate(used):
        if i == 0: 
            match used[1]:
                case u.u:
                    direction = 'u'
                    g,b = 0,2
                case u.d:
                    direction = 'd'
                    g,b = 0,2
                case u.l:
                    direction = 'l'
                    g,b = 1,3
                case u.r:
                    direction = 'r'
                    g,b = 1,3
            continue
        
        good, bad = u.get(t[g]), u.get(t[b])

        if bad.v == '.':
            bad.v = '2'
        if good.v in ['.','2']:
            good.v = '1'
        

        match used[i-1]:
            case u.d:
                nd = 'u'
            case u.u:
                nd = 'd'
            case u.l:
                nd= 'r'
            case u.r:
                nd = 'l'
        
        if direction == nd:
            pass
        else:
            print(f'{t[g]},{t[b]}',end=' ')
            g = g + x[p[direction][nd]]
            b = b + x[p[direction][nd]]
            if b > 3 or b < 0:
                b = y[b]
            if g > 3 or g < 0:
                g = y[g]

            print(f'{direction}: {nd} turn {p[direction][nd]} - new {t[g]},{t[b]}')
            direction = nd
        
        good, bad = u.get(t[g]), u.get(t[b])

        if bad.v == '.':
            bad.v = '2'
        if good.v in ['.','2']:
            good.v = '1'
        # if bad.v == '.':
        #     bad.v = '2'
   
    for line in maze:
        for ch in line:
            print(ch,end='')
        print()





fn = "2023/resources/input_10.txt"
fnt = "2023/resources/test10.txt"

print(f"pt1: {main(fnt)}")  # \npt2: {main(fn)}')
