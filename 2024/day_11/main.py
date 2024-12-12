
def day_11(fn, pt1=True):
    with (open(fn) as f):
        stones = f.read().split()
    f.close()

    if pt1:
        ans = 0
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
            print(len(s))
            ans += len(s)
        print(ans)
    else:
        ans = 0
        maxx = 0

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
    print(ans)

filename = '../resources/input_11.txt'
day_11(filename,False)