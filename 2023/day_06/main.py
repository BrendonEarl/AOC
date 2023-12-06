from math import prod, floor, ceil


def main(filename, pt2=True):
    with open(filename) as f:
        times = (
            [int(f.readline().replace(" ", "").strip().split(":")[1])]
            if pt2
            else [int(x) for x in f.readline().strip().split(":")[1].strip().split()]
        )
        dists = (
            [int(f.readline().replace(" ", "").strip().split(":")[1])]
            if pt2
            else [int(x) for x in f.readline().strip().split(":")[1].strip().split()]
        )
        f.close()

    numWaysToWin = []
    for i, time in enumerate(times):
        wins = 0 if time % 2 else -1
        minDist = dists[i]
        l, r = (
            floor(time / 2),
            ceil(time / 2)
        )

        while l * r > minDist:
            wins += 2
            l, r = l - 1, r + 1

        numWaysToWin.append(wins)

    return prod(numWaysToWin)


fn = "2023/resources/input_06.txt"
fnt = "2023/resources/test.txt"

print(f"pt1: {main(fn,False)}\n" 
      f"pt2: {main(fn)}")
