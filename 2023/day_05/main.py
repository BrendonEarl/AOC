from math import pow
import numpy as np


def main(filename):
    with open(filename) as f:
        lines = [[[y.strip() for y in x.strip().split(':')] for x in line.split('\n')] for line in f.read().split('\n\n')]
    # print(lines[0])
    # print(lines[1:])
    seeds = [int(z) for z in lines[0][0][1].split(' ')]
    lines = lines[1:]
    
    print(f'{seeds}')

    maps = []
    for line in lines:
        desc = line[0][0]
        test = [[[int(c) for c in b.split()] for b in a][0] for a in line[1:]]
        maps.append(test)
    
    # [print(m) for m in maps]

    smins = []
    for seed in seeds:
        val = seed
        
        for rule in maps:
            flag = False
            if flag: break
            for [end,start,l] in rule:
                if (val in range(start,start+l)):
                    flag=True
                    print(f'{val} in range {start},{start+l}',end='')
                    diff = start - end
                    val -= diff
                    print(f'.   newval = {val}')
                    break
        print()
        smins.append(val)
    print(min(smins))
    

        


def part2(filename):
    pass


fn = '2023/resources/input_05.txt'
fnt = '2023/resources/test.txt'

print(f'pt1: {main(fnt)}\n')
    #   f'pt2: {part2(fn)}')