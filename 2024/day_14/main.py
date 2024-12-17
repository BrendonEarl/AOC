from math import prod

def day_14(fn, pt1=True):
    with open(fn) as f:
        pv = [ [tuple(int(m) for m in l.split('=')[1].split(',')) for l in line.strip().split()] for line in f.readlines()]
    f.close()
    # maxrow, maxcol = 102, 100
    # midrow, midcol = 51, 50
    maxrow, maxcol = 6, 10
    midrow, midcol = 3, 5
    tots = [
        0, 0,
        0, 0
    ]
    for p,v in pv:
        col, row = p
        vcol, vrow = v
        ecol,erow = (col + (100 * vcol)) % maxcol, (row + (100 * vrow)) % maxrow
        # print((erow,ecol))
        if ecol < midcol:
            if erow > midrow:
                tots[2] += 1
            elif erow < midrow:
                tots[0] += 1
        elif ecol > midcol:
            if erow > midrow:
                tots[3] += 1
            elif erow < midrow:
                tots[1] += 1
    col, row = 2, 4
    vcol, vrow = 2, -3
    for i in range(6):
        ecol, erow = (col + (i * vcol)) , (row + (i * vrow))
        
        ecol, erow = ecol % maxcol, erow % maxrow
        print(f"{i} => {(ecol,erow)}")
    # print(prod(tots))
    # print(tots)



filename = '../resources/input_14.txt'
t = '../resources/test_14.txt'
day_14(t)
# 225371250 too low