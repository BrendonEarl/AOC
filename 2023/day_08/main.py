import time

lr = {
    'L' : 0,
    'R' : 1,
}

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
            if key[0][-1] == 'A':
                start.append(key[0])
        
        loops = []
        ml = len(instructions)
        for x,s in enumerate(start):
            t = 0
            ts = d[s][lr[instructions[0]]]
            n,i=1,1

            while (ts != s):
                
                if ts[-1] == 'Z':
                    t = n
                    break
                    
                ts = d[ts][lr[instructions[i]]]
                i += 1
                if i == ml: i = 0
                n += 1
                
            loops.append(t)
        mult = [loop for loop in loops]
        count = 0
        

        while not all([m==mult[0] for m in mult]):
            count += 1
            if not count % 1000000: print(f'{mult}: {int(count/1000000)}')
            
            m=max(mult)
            for i, x in enumerate(mult):
                if x < m:
                    mult[i] += loops[i]
        
        print(f'{round(time.time()-stime)/60} mins')
        return mult[0]
    

fn = '2023/resources/input_08.txt'
fnt = '2023/resources/test.txt'

print(f'pt1: {main(fn, True)} \n'
      f'pt2: {main(fn)}')