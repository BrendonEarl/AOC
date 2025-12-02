
def main(filename, pt1=True):
    with (f:=open(filename)):
        ranges = [[int(y) for y in x.split('-')] for x  in f.read().split(',')]
        ranges = [range(z[0],z[1]+1) for z in ranges]
    f.close()
    answer = 0

    if pt1:
        for r in ranges:
            for val in r:
                sval = str(val)
                if (l:=len(sval)) % 2:
                    continue
                if sval[:(l//2)] == sval[(l//2):]:
                    answer += val
    else:
        for r in ranges:
            for val in r:
                sval = str(val)
                l = len(sval)
                doadd = False
                for i in range(1,(l//2)+1):
                    if doadd:
                        break
                    if l % i:
                        continue
                    numchecks = l//i
                    pat = sval[:i]

                    badflag = False
                    for j in range(2,numchecks+1):
                        if badflag:
                            break
                        if pat != sval[(j - 1) * i:j * i]:
                            badflag = True
                            break
                    if not badflag:
                        doadd = True
                if doadd:
                    answer += val
    return answer

filename = '../resources/input_02.txt'
main(filename, False)
print(f'pt1: {main(filename)}\n'
      f'pt2: {main(filename,False)}')