from itertools import count

def day_01(fn, pt2 = True):
    f = open(fn)
    lines = f.read().strip().split()
    f.close()
    l,r = lines[::2], lines[1::2]

    tot = 0
    if pt2:
        for val in l:
            tot += r.count(val) * int(val)
        return tot
    else:
        l = sorted(l)
        r = sorted(r)
        while len(l):
            lv,rv = l.pop(),r.pop()
            tot += abs(int(lv)-int(rv))
        return tot


filename = '../resources/input_01.txt'
print(f"pt1: {day_01(filename, False)}\n"
      f"pt2: {day_01(filename)}")
