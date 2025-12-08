def main(filename, pt2=True):
    with (f:=open(filename)):
        lines = [[y for y in x.strip()] for x in f.readlines()]
    f.close()

    nrows, ncols = len(lines), len(lines[0])
    answer = 0

    if pt2:
        copy = lines.copy()

        while True:
            track = []
            for r in range(nrows):
                for c in range(ncols):
                    if copy[r][c] == '@' and isAccessible(copy,r,c):
                        answer += 1
                        track.append((r,c))

            if len(track) == 0:
                break
            for tr,tc in track:
                copy[tr][tc] = '.'
    else:
        for r in range(nrows):
            for c in range(ncols):
                if lines[r][c] == '@' and isAccessible(lines,r,c):
                    answer += 1
    return answer

def isAccessible(lines, row, col):
    nrows, ncols = len(lines), len(lines[0])
    count, checkSpots = 0, []
    rowgtzero, colgtzero, colnotmax, rownotmax = row > 0, col > 0, col < ncols - 1, row < nrows -1

    if rowgtzero:
        checkSpots.append((row-1,col))
        if colgtzero:
            checkSpots.append((row - 1, col - 1))
        if colnotmax:
            checkSpots.append((row - 1, col + 1))
    if colgtzero:
        checkSpots.append((row, col - 1))
    if colnotmax:
        checkSpots.append((row, col + 1 ))
    if rownotmax:
        checkSpots.append((row + 1, col))
        if colgtzero:
            checkSpots.append((row + 1, col - 1))
        if colnotmax:
            checkSpots.append((row + 1, col + 1))
    for kr,kc in checkSpots:
        if lines[kr][kc] == '@':
            count += 1
    return count < 4


filename = '../resources/input_04.txt'
# filename = '../resources/test_04.txt'

print(f'pt1: {main(filename, False)} \n'
      f'pt2: {main(filename)}')

# main(filename)