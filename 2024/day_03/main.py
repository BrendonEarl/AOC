from re import findall
from math import prod

def day_03(fn, pt1=True):
    with open(fn) as f:
        text = f.read()
    f.close()

    if pt1:
        x = findall("mul\(\d+,\d+\)",text)
    else:
        y = findall("mul\(\d+,\d+\)|don't\(\)|do\(\)",text)

        do_mult, x = True, []
        while len(y):
            val = y.pop(0)
            if val == 'do()':
                do_mult = True
            elif val == 'don\'t()':
                do_mult = False
            elif do_mult:
                x.append(val)

    t = [[int(y) for y in s.strip('mul(').strip(')').split(',')] for s in x]
    ans = sum(prod(m) for m in t)

    return ans


filename = '../resources/input_03.txt'
print(f"pt1: {day_03(filename)}\n"
      f"pt2: {day_03(filename,False)}")