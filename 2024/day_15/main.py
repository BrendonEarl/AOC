
class day_15():

    def __init__(self, fn):
        with open(fn) as f:
            mapp, moves = [[l for l in line.strip().split('\n')] for line in f.read().split('\n\n')]
        f.close()
        print(mapp)
        moves = ''. join(moves)
        print(moves)


filename = '../resources/test_15.txt'
t15 = day_15(filename)