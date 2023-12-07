ranks = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2,
}


def main(filename, pt1=False):
    if not pt1: ranks['J'] = 1
    with open(filename) as f:
        lines = [line.strip().split() for line in f]
    f.close()

    for i, [hand,bet] in enumerate(lines):
        lines[i] = [[ranks[x] for x in hand],bet]

    five, four, full, three, tpair, two, high = [],[],[],[],[],[],[]

    for line in lines:
        hand,bet = line
        r,nwilds = [],0
        for j, num in enumerate(hand):
            numsame = 1
            if num == 1:
                nwilds += 1 
            for k, t in enumerate(hand):
                if j==k: continue
                numsame += 1 if num==t else 0

            r.append(numsame)
        r = sorted(r)
        
        if pt1 or (not nwilds):
            if (5 in r):
                five.append(line)
            elif (4 in r):
                four.append(line)
            elif (3 in r):
                if(2 in r):
                    full.append(line)
                else:
                    three.append(line)
            elif(2 in r):
                count=0
                for x in r:
                    count += 1 if x==2 else 0
                if(count==4):
                    tpair.append(line)
                elif(count==2):
                    two.append(line)
            else:
                high.append(line)
        else:
            for i in range(nwilds):
                r.remove(nwilds)
            
            if(r):
                w = r[-1] 
            else:
                five.append(line)
                continue

            if (w + nwilds == 5):
                five.append(line)
            elif(w + nwilds == 4):
                four.append(line)
            elif(2 in r):
                count=0
                for x in r:
                    count += 1 if x==2 else 0
                if count == 4 :
                    full.append(line)
                elif count ==2:
                    if nwilds == 1:
                        three.append(line)
            else:
                if(w + nwilds == 3):
                    three.append(line)
                else:
                    two.append(line)

    test = [high,two,tpair,three,full,four,five]
    for z,tes in enumerate(test):
        test[z] = sorted(tes)

    s,i = 0,1
    for y in test:
        for _,x in y:
            s += int(x)*i
            i += 1
    return s

    

fn = "2023/resources/input_07.txt"
fnt = "2023/resources/test.txt"

print(f"pt1: {main(fn,True)}\n"
      f"pt2: {main(fn)}")