import numpy as np
from math import floor
import sys
from time import sleep
np.set_printoptions(threshold=sys.maxsize)

IN, OUT = 1, 0 #switch if not working
dirs = {
    'l' : ['u', 'd'],
    'u' : ['r', 'l'],
    'r' : ['d', 'u'],
    'd' : ['l', 'r']
}
class Cell:

    def __init__(self, v) -> None:
        self.v = v
        self.l, self.u, self.r, self.d = None, None, None, None
        self.connections = []
        self.inLoop = False
        self.b, self.a = None,None
        self.ind, self.outd = '', ''
        self.ins = []


    def setNeighbors(self, l: "Cell", u: "Cell", r: "Cell", d: "Cell"):
        self.l, self.u, self.r, self.d = l, u, r, d
        self.setConnections()

    def setDirections(self):
        t = {
            self.l : ['r', 'l'],
            self.u : ['d', 'u'],
            self.r : ['l', 'r'],
            self.d : ['u', 'd'],
        }
        self.ind = t[self.b][0]
        self.outd = t[self.a][1]
            
        self.ins.append(dirs[self.ind][IN])
        if self.ind != self.outd:
            self.ins.append(dirs[self.outd][IN])

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
        return {
            'l' : self.l,
            'u' : self.u,
            'r' : self.r,
            'd' : self.d
        }[s]
    
    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.v


def main(fn, pt1=False):
    with open(fn) as f:
        lines = [[*line.strip()] for line in f]
    f.close

    maze = np.array(lines, dtype=object)

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
    s = maze[startr][startc]
    check = s.connections[0]
    s.a, check.b = check, s
    s.inLoop, check.inLoop = True, True

    while check != s:
            
        one, two = check.connections
        if not one.inLoop:
            nxt = one
        elif not two.inLoop:
            nxt = two
        else:
            check.a = s
            s.b = check
            break

        nxt.inLoop = True
        check.a, nxt.b = nxt, check
        check = nxt
    
    if pt1:
        check = s.a
        summ = 1
        while check != s:
            nxt = check.a
            summ +=1 
            check = nxt
        return int(floor(summ/2))

    for line in maze:
        for ch in line:
            if not ch.inLoop:
                ch.v = '.'
                ch.connections = []
            print(ch,end='')
        print()
 
    check = s
    while True:
        check.setDirections()
        for letter in check.ins:
            test = check.get(letter)
            if not test.inLoop:
                test.v = 'I'
        check = check.a
        if check == s:
            break
    
    for line in maze:
        for j, ch in enumerate(line):
            if ch.v == '.':
                chain = [ch]
                nxt = ch.r
                while nxt and nxt.v == '.':
                    chain.append(nxt)
                    nxt = nxt.r
                
                if nxt and nxt.v == 'I':
                    for c in chain:
                        c.v = 'I'
                else:
                    for c in chain:
                        c.v = 'O'
    
    print()
    pt2 = 0
    for line in maze:
        for ch in line:
            if ch.v == 'I':
                pt2 += 1
            if ch.inLoop:
                ch.v = '-'
            print(ch,end='')
        print()
    
    return pt2


fn = "2023/resources/input_10.txt"

print(f"pt1: {main(fn, True)}\npt2: {main(fn)}")