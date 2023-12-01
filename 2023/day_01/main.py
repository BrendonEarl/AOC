map = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}

def part1(filename):
    test = [line.strip() for line in open(filename).readlines()]
    sum = 0
    
    for y in test:
        found = False
        first = 0
        last = 0
        for z in y:
            if(z.isnumeric()):
                if not found:
                    first = int(z)
                    found = True
                last = int(z)
        sum += (first * 10 ) + last
    print(sum)

def main(filename):
    test = [line.strip() for line in open(filename).readlines()]
    sum = 0

    for line in test:
        first = 0
        last = 0
        for index, char in enumerate(line):
            if(char.isnumeric()):
                if not first:
                    first = int(char)
                last = int(char)
            for i in range(3,6):
                try:
                    if not first:
                        first = map[line[index:index+i]]
                    last = map[line[index:index+i]]
                except:
                    KeyError
        sum += (first * 10 ) + last
    print(sum)
                    
f = '2023/resources/input_01.txt'
part1(f)
main(f)