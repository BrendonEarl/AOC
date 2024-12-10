
class day_10():

    def __init__(self, fn):
        with open(fn) as f:
            self.mapp = [list(map(int, line.strip())) for line in f.readlines()]
        f.close()

    def solve(self):
        trailheads = []
        for i in range(len(self.mapp)):
            for j in range(len(self.mapp[0])):
                if not self.mapp[i][j]:
                    trailheads.append((i, j))
        ans1, ans2 = 0, 0

        for row, col in trailheads:
            arr = self.solveHelper(row, col, self.mapp[row][col], 0)
            ans2 += len(arr)
            distinct = []
            for y in arr:
                if y not in distinct:
                    distinct.append(y)
            ans1 += len(distinct)
        return ans1, ans2

    def solveHelper(self, row, col, val, expected):
        if val != expected:
            return False
        if val == 9 and expected == 9:
            return row, col

        countt = []
        if row > 0 and (u := self.solveHelper(row - 1, col, self.mapp[row - 1][col], expected + 1)):
            if isinstance(u, list):
                countt = countt + u
            else:
                countt.append(u)
        if row < len(self.mapp) - 1 and (d := self.solveHelper(row + 1, col, self.mapp[row + 1][col], expected + 1)):
            if isinstance(d, list):
                countt = countt + d
            else:
                countt.append(d)
        if col > 0 and (l := self.solveHelper(row, col - 1, self.mapp[row][col - 1], expected + 1)):
            if isinstance(l, list):
                countt = countt + l
            else:
                countt.append(l)
        if col < len(self.mapp[0]) - 1 and (r := self.solveHelper(row, col + 1, self.mapp[row][col + 1], expected + 1)):
            if isinstance(r, list):
                countt = countt + r
            else:
                countt.append(r)

        return countt


filename = '../resources/input_10.txt'
test = '../resources/test_10.txt'
one, two = day_10(filename).solve()
print(f"pt1: {one}\n"
      f"pt2: {two}")
