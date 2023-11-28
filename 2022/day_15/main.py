

def main(filename):
    arr = [line.strip() for line in open(filename).readlines()]


real = '2022/resources/input_15.txt'
test = '2022/resources/input_15_test.txt'

main(real)