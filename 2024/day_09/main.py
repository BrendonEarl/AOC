
def day_09(fn, pt1=True):
    with open(fn) as f:
        x = f.read()
        blocks = x[::2]
        freespace = x[1::2]
    f.close()

    if pt1:
        l,r = 0, len(blocks)-1
        pos = 0
        ans = 0
        endval = int(blocks[r])
        while l < r:
            for i in range(int(blocks[l])):
                ans += l * pos
                pos += 1

            numfree = int(freespace[l])
            l+=1
            if not l <= r:
                break
            for i in range(numfree):
                if endval:
                    ans += r * pos
                    pos += 1
                    endval -= 1
                else:
                    r-=1
                    while blocks[r] == '0':
                        r -= 1
                    if r <= l:
                        break
                    endval = int(blocks[r])
                    ans += r * pos
                    pos += 1
                    endval -= 1
        for i in range(endval):
            ans += l * pos
            pos += 1

        return ans
    else:
        structure = []
        for i in range(len(blocks)):
            structure.append([i for j in range(int(blocks[i]))])
            if i < len(blocks)-1:
                structure.append(int(freespace[i]))

        for i in range(len(structure)-1,-1,-1):

            tomove = structure[i]
            if not isinstance(tomove, int):
                ln = len(tomove)

                for j in range(i):
                    fit = structure[j]
                    if isinstance(fit, int) and ln<=fit:
                        if ln==fit:
                            structure[i] = ln
                            structure[j] = tomove
                        else:
                            structure[i] = ln
                            structure[j] -=ln
                            structure.insert(j,tomove)
                        break

        pos = 0
        ans = 0
        for s in structure:
            if isinstance(s,int):
                pos += s
            else:
                for val in s:
                    ans += (pos * val)
                    pos+=1
        return ans

filename = '../resources/input_09.txt'
t = '../resources/test_09.txt'
print(f"pt1: {day_09(filename)}\n"
      f"pt2: {day_09(filename,False)}")