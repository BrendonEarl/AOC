
def day_08(fn, pt1=True):
    with open(fn) as f:
        arr = [[l for l in line.strip()] for line in f.readlines()]
        track = [[0 for l in line] for line in arr]
    f.close()

    frequencies = {}
    for row,rowvals in enumerate(arr):
        for col,val in enumerate(rowvals):
            if val == '.' or val =='#':
                continue

            x = frequencies.get(val)
            if x is None:
                frequencies[val] = [(row,col)]
            else:
                x.append((row,col))

    minr, minc, maxr, maxc = 0, 0, len(arr)-1, len(arr[0])-1
    for key in frequencies:
        coords = frequencies.get(key)
        if len(coords) < 2: continue
        for x in range(len(coords)-1):
            for y in range(x+1, len(coords)):
                r1,c1 = coords[x]
                r2,c2 = coords[y]
                sloper,slopec = r2-r1, c2-c1
                if pt1:
                    if r1 - sloper >= minr and r1-sloper <= maxr and c1-slopec >= minc and c1-slopec <=maxc:
                        track[r1-sloper][c1-slopec] = 1
                    if r2 + sloper >= minr and r2+sloper <= maxr and c2+slopec >= minc and c2+slopec <=maxc:
                        track[r2+sloper][c2+slopec] = 1
                else:
                    track[r1][c1] = 1
                    track[r2][c2] = 1
                    i = 1
                    while r1 - (sloper * i) >= minr and r1-(sloper * i) <= maxr and c1-(slopec * i) >= minc and c1-(slopec * i) <=maxc:
                        track[r1 - (sloper * i)][c1 - (slopec * i)] = 1
                        i += 1

                    i = 1
                    while r2 + (sloper * i) >= minr and r2+(sloper * i) <= maxr and c2+(slopec * i) >= minc and c2+(slopec * i) <=maxc:
                        track[r2+(sloper * i)][c2+(slopec * i)] = 1
                        i+=1

    return sum(sum(line) for line in track)

filename = '../resources/input_08.txt'
t = '../resources/test_08.txt'
print(f"pt1: {day_08(filename)}\n"
      f"pt2: {day_08(filename,False)}")