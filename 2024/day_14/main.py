from math import prod, floor


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
        ecol,erow = (col + (100 * vcol)), (row + (100 * vrow))
        test = ''

        if ecol > 0:
            ecol = ((ecol - 1) % maxcol) + 1
        elif ecol == 0:
            pass
        else:
            test = floor(ecol / maxcol)
            while ecol < 0:
                ecol += maxcol
            ecol = (ecol+test)%maxcol

        if erow > 0:
            erow = ((erow - 1) % maxrow) + 1
        elif erow == 0:
            pass
        else:
            test = -1 * floor(erow / maxrow)
            while erow < 0:
                erow += maxrow
            erow = (erow + test)%maxrow

        print((ecol, erow, test))
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

    print(prod(tots))
    print(tots)




filename = '../resources/input_14.txt'
t = '../resources/test_14.txt'
day_14(t)
# 225371250 too low