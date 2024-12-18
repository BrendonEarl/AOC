from math import prod

def day_14(fn, pt1=True):
    with open(fn) as f:
        pv = [ [tuple(int(m) for m in l.split('=')[1].split(',')) for l in line.strip().split()] for line in f.readlines()]
    f.close()
    maxrow, maxcol = 103, 101
    midrow, midcol = 51, 50

    tots = [
        0, 0,
        0, 0
    ]
    if pt1:
        for p,v in pv:
            col, row = p
            vcol, vrow = v
            ecol,erow = (col + (100 * vcol)) % maxcol, (row + (100 * vrow)) %maxrow

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
        return prod(tots)
    else:

        for i in range(100000):
            test = [['.' for c in range(maxcol)] for r in range(maxrow)]
            for p, v in pv:
                col, row = p
                vcol, vrow = v
                ecol, erow = (col + (i * vcol)) % maxcol, (row + (i * vrow)) % maxrow
                test[erow][ecol] = '#'
            if any(['###############################' in ''.join(ro) for ro in test]):

                [print(''.join(te)) for te in test]
                return i


filename = '../resources/input_14.txt'
t = '../resources/test_14.txt'
print(f"pt1: {day_14(filename)}\n"
      f"pt2: {day_14(filename, False)}")
