import time

lr = {
    'L' : 0,
    'R' : 1,
}
END = 2
def main(fn, pt1=False):
    d = {}
    with open(fn) as f:
        lines = [line.strip() for line in f]
        instructions, lines = lines[0], lines[2::]
        instructions = [instruction for instruction in instructions]
        lines = [[[m.strip().replace('(','').replace(')','') for m in l.strip().split(',')] for l in line.strip().split('=')] for line in lines]
        
        for key, vals in lines:
            d[key[0]] = vals

    f.close()

    if pt1:
        start, n, i, ml = 'AAA', 0, 0, len(instructions)

        while start != 'ZZZ':
            if i == ml:
                i = 0
            start = d[start][lr[instructions[i]]]
            n += 1
            i += 1
        return n
    else:
        stime = time.time()
        start = []
        for key, _ in lines:
            if key[0][END] == 'A':
                start.append(key[0])
        
        loops = [[] for s in start]
        ml = len(instructions)
        for x,s in enumerate(start):
            t = []
            ts = d[s][lr[instructions[0]]]
            n,i=0,1
            used = []
            print(f'{s} {ts}')
            while ts != s:
                if i == ml:
                    i = 0
                if ts not in used:
                    print(f'{n} iterations \n{ts} \nused: {used}')
                    used.append(ts)
                if ts[-1] == 'Z':
                    t.append(n)
                    print(f'--------------------{n}: {t}: {used}')
                ts = d[s][lr[instructions[i]]]
                i += 1
                n += 1
                
            print(t)
                

            print(f'{x} : {s}')

        # n, i, ml = 0, 0, len(instructions)
        # while not all(map(lambda x: x[END]=='Z', start)):
        #     if i == ml:
        #         i = 0
        #     if n%10000000==0:
        #         print(f'{n} => {start} {time.time() - stime}')
        #     start = [d[s][lr[instructions[i]]] for s in start]
        #     n += 1
        #     i += 1

        # return n
    



fn = '2023/resources/input_08.txt'
fnt = '2023/resources/test.txt'

print(f'pt1: {main(fn)} \n')
    #   f'pt2: {main(fn,False)}')