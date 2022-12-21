

def main(filename):
    arr = [line.strip() for line in open(filename).readlines()]


real = 'resources/input_15.txt'
test = 'resources/input_15_test.txt'

main(real)