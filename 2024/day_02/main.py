def day_02(fn, pt1=True):
    f = open(fn)
    arr = [[int(y) for y in x.strip().split()] for x in f.readlines()]
    f.close()

    tot = 0
    for line in arr:
            if isSafe(line):
                tot += 1
            elif not pt1:
                tests = [[x  for j,x in enumerate(line) if j!=i] for i in range(len(line))]
                tot += 1 if any(isSafe(test) for test in tests) else 0
    return tot


def isSafe(line, max_diff=3):
    line_pos = line[1] - line[0] > 0
    for i in range(len(line) - 1):
        diff = line[i + 1] - line[i]
        if diff:
            if abs(diff) > max_diff:
                return False
            if (diff < 0 and line_pos) or (diff > 0 and not line_pos):
                return False
        else:
            return False
    return True

filename = '../resources/input_02.txt'
print(f"pt1: {day_02(filename)}\n"
      f"pt2: {day_02(filename,False)}")
