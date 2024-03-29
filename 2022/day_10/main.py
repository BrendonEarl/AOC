import math
def main(filename):
    arr = [line.strip().split() for line in open(filename).readlines()]

    [print(line) for line in arr]

    cycle, x = 1, 1
    k = {
        'addx' : 2,
        'noop' : 1
    }
    checks = [20, 60, 100, 140, 180, 220]
    screen = [[],[],[],[],[],[]]

    for command in arr:
        name = command[0]
        
        for _ in range(k[command[0]]):
            print(f'===============cycle {cycle % 40}: x={x} : cyclex = {int(math.floor((cycle-1)/40))} : {(cycle % 40) in [x-1,x,x+1]}')
            screen[int(math.floor((cycle-1)/40))].append('#' if (cycle%40)-1 in [x-1,x,x+1] else '.')
            cycle += 1
        
        if name == "addx": x += int(command[1])
    
    for line in screen:
        for character in line:
            print(character,end='')
        print('')


main('2022/resources/input_10.txt')
#720 too low