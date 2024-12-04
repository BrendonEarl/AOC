from itertools import count


def day_04(fn, pt1 = True):
    with open(fn) as f:
        x = [l.strip() for l in f.readlines()]
        chars = [list(map(lambda q:q, y)) for y in x]
    f.close()

    min_row, min_col, max_row, max_col = 0, 0, len(chars)-1, len(chars[0])-1

    if pt1:
        answer, s, di = 0, 'XMAS', [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        for r, vals in enumerate(chars):
            for c, val in enumerate(vals):

                for d in di:
                    rt,ct = d
                    bf = False
                    for i in range(4):
                        nr,nc = r + (rt*i), c + (ct*i)

                        if nr < min_row or nr > max_row or nc < min_col or nc > max_col:
                            bf = True
                            break
                        if s[i] != chars[nr][nc]:
                            bf = True
                            break

                    if not bf:
                        answer += 1
    else:
        answer = 0
        for r, vals in enumerate(chars):
            if r == min_row or r == max_row:
                continue
            for c, val in enumerate(vals):
                if c == min_col or c == max_col:
                    continue

                if val == 'A':
                    one = [chars[r - 1][c - 1], chars[r + 1][c + 1]]
                    two = [chars[r - 1][c + 1], chars[r + 1][c - 1]]

                    answer += 1 if (one.count('M') == 1 and one.count('S') == 1 and two.count('M') == 1 and two.count('S') == 1) else 0
    return answer


filename = '../resources/input_04.txt'
t = '../resources/test_04.txt'
print(f"pt1: {day_04(filename)}\n"
      f"pt2: {day_04(filename, False)}")
