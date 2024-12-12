
def day_11(fn, pt1=True):
    with (open(fn) as f):
        stones = f.read().split()
    f.close()

    ans = 0
    if pt1:
        for stone in stones:
            s = [stone]
            for i in range(25):
                new = []
                while len(s):
                    x = s.pop(0)
                    if not len(x) % 2:
                        half = int(len(x)/2)
                        l,r = x[:half], x[half:]
                        new.append(str(int(l)))
                        new.append(str(int(r)))
                    elif x == '0':
                        new.append('1')
                    else:
                        new.append(str(2024 * int(x)))
                s = new

            ans += len(s)
        return ans
    else:
        for stone in stones:
            steps = {}
            s = [stone]
            while len(s):
                new = []
                while len(s):
                    x = s.pop(0)

                    if not len(x) % 2:
                        half = int(len(x) / 2)
                        l, r = x[:half], x[half:]
                        steps[x] = [str(int(l)), str(int(r))]
                        new.append(str(int(l)))
                        new.append(str(int(r)))
                    elif x == '0':
                        new.append('1')
                        steps[x] = ['1']
                    else:
                        new.append(y:=str(2024 * int(x)))
                        steps[x] = [y]
                s = list(filter(lambda z : z not in steps.keys(), new))

            track = {}
            for step in steps.keys():
                track[step] = 0
            track[stone] = 1

            for i in range(75):
                ntrack = {}

                for p in track.keys():
                    n = track[p]
                    vals = steps[p]
                    for val in vals:
                        if ntrack.get(val) is not None:
                            ntrack[val] += n
                        else:
                            ntrack[val] = n
                track = ntrack
            ans += sum(track.values())
    return ans

filename = '../resources/input_11.txt'
print(f"pt1: {day_11(filename)}\n"
      f"pt2: {day_11(filename,False)}")
day_11(filename,False)