
def day_06(fn, pt1 = True):
    with open(fn) as f:
        blueprint = [line.strip('\n') for line in f.readlines()]
        track = [[l for l in line] for line in blueprint]
    f.close()

    xy,di = (0,0), ''
    dirs = {
        '<' : (0,-1),
        '>' : (0,1),
        '^' : (-1,0),
        'v' : (1,0)
    }
    nxtdir = {
        '<' : '^',
        '^' : '>',
        '>' : 'v',
        'v' : '<'
    }

    for i in range(len(blueprint)):
        for j in range(len(blueprint[i])):
            if blueprint[i][j] in ['<', '>', 'v', '^']:
                xy = (i,j)
                di = blueprint[i][j]

    minr, minc, maxr, maxc = 0, 0, len(blueprint)-1, len(blueprint[0])-1
    must_turn = lambda coord,d,bp : bp[coord[0] + dirs[d][0]][coord[1] + dirs[d][1]] == '#'
    do_end = lambda coord,d : (coord[0] == minr and d == '^') or (coord[0] == maxr and d == 'v') or (coord[1] == minc and d == '<') or (coord[1] == maxc and d == '>')

    if pt1:
        while not do_end(xy,di):
            x,y = xy
            track[x][y] = 'x'
            if must_turn(xy,di,blueprint):
                di = nxtdir[di]
            else:
                xy = (x+dirs[di][0],y+dirs[di][1])
                track[xy[0]][xy[1]] = 'x'

        ans = 0
        for i in range(len(track)):
            for j in range(len(track[0])):
                ans += 1 if track[i][j] == 'x' else 0
        return ans
    else:
        ans = 0
        distinct = [[True for l in line] for line in blueprint]
        while not do_end(xy, di):
            x, y = xy
            distinct[x][y] = False
            track[x][y] = 'x'
            if must_turn(xy, di, blueprint):
                di = nxtdir[di]
            else:
                testtrack = [[l for l in line] for line in blueprint]
                dtrack = [[[] for l in line] for line in blueprint]
                testxy = (x,y)
                testdi = nxtdir[di]
                if distinct[x+dirs[di][0]][y+dirs[di][1]]:
                    distinct[x + dirs[di][0]][y + dirs[di][1]] = False
                    testtrack[x+dirs[di][0]][y+dirs[di][1]] = '#'
                else:
                    xy = (x + dirs[di][0], y + dirs[di][1])
                    continue

                does_loop = False
                while not do_end(testxy, testdi):

                    if testdi in dtrack[testxy[0]][testxy[1]]:
                        does_loop = True
                        break
                    dtrack[testxy[0]][testxy[1]].append(testdi)
                    if must_turn(testxy, testdi, testtrack):
                        testdi = nxtdir[testdi]
                    else:
                        testxy = (testxy[0] + dirs[testdi][0], testxy[1] + dirs[testdi][1])

                if does_loop:
                    distinct[x + dirs[di][0]][y + dirs[di][1]] = False
                    ans += 1

                xy = (x + dirs[di][0], y + dirs[di][1])
        return ans

filename = '../resources/input_06.txt'
t = '../resources/test_06.txt'
print(f"pt1: {day_06(filename)}\n"
      f"pt2: {day_06(filename,False)}")