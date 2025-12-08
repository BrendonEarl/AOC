
def main(filename, pt2=True):
    with (f:=open(filename)):
        ranges,ids = f.read().split('\n\n')
        ranges = [[int(y) for y in x.strip().split('-')] for x in ranges.split('\n')]

        ids = [int(x) for x in ids.split('\n')]
    f.close()
    answer = 0

    if pt2:
        killList = []
        fightList = []
        for i,r in enumerate(ranges):
            for j,tr in enumerate(ranges):
                if j <= i: continue
                l1,r1 = r
                l2,r2 = tr
                if (l1 < l2 and r1 < l2) or (l1 > r2 and r1 > r2): continue
                if l1 <= l2 and r1 >=r2:
                    killList.append(j)
                    print(f'{r} contains {tr}')
                    continue
                if l1 >= l2 and r1<=r2:
                    killList.append(i)
                    print(f'{r} is contained in {tr}')
                    continue

                print(f'{r} intersects {tr}')
                fightList.append((i,j))

        for l,h in fightList:
            if l in killList or h in killList: continue
            r,tr = ranges[l],ranges[h]
            l1, r1 = r
            l2, r2 = tr
            if (l1 < l2 and r1 < l2) or (l1 > r2 and r1 > r2): continue
            if  r1 < r2:
                r1 = l2 - 1
            else:
                l1 = r2 +1
            ranges[l] = [l1,r1]

        for index in killList:
            ranges[index] = None

        ranges = list(filter(lambda x: x is not None ,ranges))
        ranges = [y+1-x for x,y in ranges]
        answer = sum(ranges)

    else:
        ranges = [range(l,h+1) for l,h in ranges]

        for num in ids:
            for r in ranges:
                if num in r:
                    answer += 1
                    break

    return answer

filename = '../resources/input_05.txt'
# filename = '../resources/test_05.txt'

print(f'pt1: {main(filename, False)} \n'
      f'pt2: {main(filename)}')

# main(filename)