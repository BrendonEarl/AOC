import operator

def main(filename, pt2=True):
    with (f:=open(filename)):
        lines = [[y[0], int(y[1:])] for y in [x.strip() for x in f]]
    f.close()

    pos, numzero = 50, 0

    if pt2:
        for d, n in lines:
            func = operator.add if d=='R' else operator.sub
            for i in range(n):
                pos = func(pos,1)
                if pos > 99:
                    pos = 0
                if pos < 0:
                    pos = 99
                if pos == 0:
                    numzero += 1
        return numzero
    else:
        for d,n in lines:
            n = n % 100
            pos = pos + n if d =='R' else pos - n
            if pos < 0:
                pos = 100 + pos
            if pos > 99 :
                pos = pos - 100
            numzero += 1 if pos == 0 else 0
        return numzero



filename = '../resources/input_01.txt'
# filename = '../resources/test_01.txt'

print(f'pt1: {main(filename, False)} \n'
      f'pt2: {main(filename)}')
main(filename)