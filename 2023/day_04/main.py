from math import pow
import numpy as np

def main(filename):
    sum, lines = 0, [[[int(w) for w in x.strip().split()] for x in [y for y in line.strip().split(':')][1].strip().split('|')] for line in open(filename)]
    for win,guess in lines:
        n = 0
        for g in guess:
            if g in win:
                n+=1
        if(n):
            sum+= pow(2,n-1)
    return int(sum)

def part2(filename):
    lines = [[[int(w) for w in x.strip().split()] for x in [y for y in line.strip().split(':')][1].strip().split('|')] for line in open(filename)]

    cards = np.ones((len(lines),), dtype=int)
    for id, [win,guess] in enumerate(lines):
        n = 0
        for g in guess:
            if g in win:
                n+=1
        
        for i in range(id+1,id+n+1):
            cards[i]+= cards[id]
    
    return int(np.sum(cards))

fn = '2023/resources/input_04.txt'
fnt = '2023/resources/test.txt'

print(f'pt1: {main(fn)}\n'
      f'pt2: {part2(fn)}')