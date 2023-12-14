
def checkVals(chars, coords, test, nums):
    check = [c for c in chars]
    
    for j, coord in enumerate(coords):
        mn, mx, ct = coord[0], coord[1], 0
        for i in range(mn,mx+1):
            if check[i] == '?':
                check[i] = test[j][ct]
            elif check[i] != test[j][ct]:
                return 0
        
            ct += 1
    
    arr = []
    p, switch, co_nt = 0, False, 0
    while p < (l:=len(check)):
        if switch:
            if check[p] == '#':
                co_nt += 1
            else:
                switch = False
                arr.append(co_nt)
                co_nt = 0
        else:
            if check[p] == '#':
                switch = True
                co_nt = 1
        p += 1
    
    if (co_nt): 
        arr.append(co_nt)
    return 1 if arr == nums else 0


def main(fn, pt2=True):
    with open(fn) as f:
        lines = [line.strip().split() for line in f]
        for i, [l,r] in enumerate(lines):
            if pt2:
                sep = "?"
                l = [*((l+sep)*5)][:-1]
                r = ((r+",")*5)
                r = [int(x) for x in r.split(',')[:-1]]
                # print(r)
            else:
                l = [*l]
                r = [int(x) for x in r.split(',')]
            lines[i] = [l,r]

    f.close()

    summ = 0
    for i,[chars,nums] in enumerate(lines):
        
        test = []
        
        for num in nums:
            t = [*num*'#']
            test.append(t)
        
        coords, start = [], 0
        for t in test:
            coords.append([start, new:=start+len(t)-1])
            start = new +1
        
        stops = [(len(chars)-sum([(b[1]-b[0]+1) for  b in coords[i:len(coords)]])) for i,_ in enumerate(coords)]
        nc, break_flag, tsum = len(coords)-1, False, 0
        
        while True:
            if break_flag: 
                break
            
            tsum+=checkVals(chars, coords, test, nums)
            for k in range(nc,-1,-1):
                while(coords[k][0] < stops[k]):
                    coords[k] = [c+1 for c in coords[k]]
                    tsum+=checkVals(chars, coords, test, nums)

                if k != 0:
                    if (coords[k-1][0]!=stops[k-1]):
                        coords[k-1] = [c+1 for c in coords[k-1]]
                        if coords[k-1][0] < stops[k-1]:
                            coords[k] = [coords[k-1][1] + 1, coords[k-1][1] + (coords[k][1]-coords[k][0])+1]
                            if k != nc:
                                coords[k+1] = [coords[k][1] + 1, coords[k][1] + (coords[k+1][1]-coords[k+1][0])+1]
                        break
                else:
                    if (coords[k][0] == stops[k]):
                        break_flag = True
                        break
        summ += tsum
    return summ
                    

fn = '2023/resources/input_12.txt'
fnt = '2023/resources/test12.txt'

print(f"pt1: {main(fn,False)}") #\npt2: {main(fn)}")