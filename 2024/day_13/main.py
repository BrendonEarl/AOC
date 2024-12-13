
def day_13(fn, pt=True):
    with open(fn) as f:
        lines = [block.split('\n') for block in f.read().split('\n\n')]
        rules = []
    f.close()
    [print(line) for line in lines]
    for A,B,P in lines:
        x,y = [int(j.split('+')[1]) for j in A.split(':')[1].strip().split(',')]
        z,q = [int(j.split('+')[1]) for j in B.split(':')[1].strip().split(',')]
        m,n = [int(j.split('=')[1]) for j in P.split(':')[1].strip().split(',')]
        print((x,y,z,q,m,n))


filename = '../resources/input_13.txt'
day_13(filename)