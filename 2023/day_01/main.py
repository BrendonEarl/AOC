

def main(filename, part1=True):
    test = [print(line, end=' ') for line in open(filename).readlines()]

real = '2023/resources/test.txt'
main(real)