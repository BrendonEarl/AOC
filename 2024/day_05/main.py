
def day_05(fn, pt2 = True):
    with open(fn) as f:
        rules,updates = f.read().split('\n\n')
        rules = [r.split('|') for r in rules.split('\n')]
        updates = [u.split(',') for u in updates.split('\n')]
    f.close()

    d = {}
    for b,a in rules:
        x = d.get(b)

        if x is None:
            d[b] = [a]
        else:
            x.append(a)

    summ = 0
    sum2 = 0
    for update in updates:
        up = update[::-1]
        bf = False

        for i in range(len(up)-1):
            if bf: break
            for j in range(i+1,len(up)):
                if up[j] in d[up[i]]:

                    bf = True
                    break


        if not bf:
            summ += int(update[int((len(update)-1)/2)])
        if pt2 and bf:

            redo = True
            while redo:
                redo = False
                for i in range(len(up)-1):
                    last = i
                    if redo:
                        continue
                    for j in range(i+1, len(up)):
                        if up[j] in d[up[i]]:
                            last = j
                            redo = True

                    if last !=i:
                        if i == 0:
                            l,m,r = [], up[i], up[i+1:]
                        else:
                            l,m,r = up[:i], up[i], up[i+1:]

                        new = l + r
                        if last == len(up)-1:
                            fin = new + [m]
                        else:
                            fin = new[:last] + [m] + new[last:]
                        up[:] = fin
            sum2 += int(up[int((len(up)-1)/2)])

    return sum2 if pt2 else summ


filename = '../resources/input_05.txt'
print(f"pt1: {day_05(filename,False)}\n"
      f"pt2: {day_05(filename)}")
