
class day_12():

    def __init__(self, fn):
        with open(fn) as f:
            self.mapp = [[l for l in line.strip()] for line in f.readlines()]
            self.track = [[0 for l in line] for line in self.mapp]
            self.groups = []
        f.close()
        self.printMap(self.mapp)

    def printMap(self, arr):
        [print(''.join(line)) for line in arr]

    def solve(self, pt1=True):
        for i in range(len(self.mapp)):
            for j in range(len(self.mapp[0])):
                if not self.track[i][j]:
                    self.groups.append([])
                    self.solveHelper(i,j,self.mapp[i][j])
        [print(g) for g in self.groups]
        ans = 0
        if pt1:
            for group in self.groups:
                area = len(group)
                perimeter = 0
                for x,y in group:

                    test = [(x + 1,y), (x - 1,y), (x,y + 1), (x,y-1)]
                    for t in test:
                        if t not in group:
                            perimeter += 1
                print(perimeter*area)
                ans += perimeter*area
        else:
            for group in self.groups:
                area = len(group)
                numSides = 0
                # todo: left toggle and right toggle
                # for i in range(len(self.mapp)):
                #     toggle = False
                #     for j in range(len(self.mapp[0])):
                #         if (i,j) in group and [(i,j + 1) not in group, (i,j-1) not in group]:
                #             if not toggle:
                #                 numSides += 1
                #             toggle = True
                #         else:
                #             toggle = False


                ans += numSides * area

        print(ans)

    def solveHelper(self, i, j, val):
        if i < 0 or i >= len(self.mapp) or j < 0 or j >= len(self.mapp[0]):
            return

        if (not self.track[i][j]) and (self.mapp[i][j] == val):
            self.track[i][j] = 1
            self.groups[-1].append((i,j))
            self.solveHelper(i + 1, j, val)
            self.solveHelper(i - 1, j, val)
            self.solveHelper(i, j + 1, val)
            self.solveHelper(i, j - 1, val)


filename = '../resources/input_12.txt'
tfile = '../resources/test_12.txt'
day_12(filename).solve(False)