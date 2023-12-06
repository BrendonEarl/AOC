def main(filename):
    with open(filename) as f:
        lines = [
            [[y.strip() for y in x.strip().split(":")] for x in line.split("\n")]
            for line in f.read().split("\n\n")
        ]

    seeds = [int(z) for z in lines[0][0][1].split(" ")]
    lines = lines[1:]

    maps = []
    for line in lines:
        test = [[[int(c) for c in b.split()] for b in a][0] for a in line[1:]]
        maps.append(test)

    smins = []
    for seed in seeds:
        val = seed

        for rule in maps:
            flag = False
            if flag:
                break
            for [end, start, l] in rule:
                if val in range(start, start + l):
                    flag = True
                    diff = start - end
                    val -= diff
                    break
        
        smins.append(val)
    return min(smins)


def splitOrReturn(s, t):
    ss, se = s
    ts, te, tval = t
    does, no = [], []

    if ss < ts:
        no.append([ss, ts - 1])
        ss = ts
    if se > te:
        no.append([te + 1, se])
        se = te
    does = [ss + tval, se + tval]

    return does, no


def part2(filename):
    with open(filename) as f:
        lines = [
            [[y.strip() for y in x.strip().split(":")] for x in line.split("\n")]
            for line in f.read().split("\n\n")
        ]

    seeds = [int(z) for z in lines[0][0][1].split(" ")]
    l, r = [seeds[::2], seeds[1::2]]
    seeds = []
    for i, v in enumerate(l):
        seeds.append([v, v + r[i] - 1])

    lines = lines[1:]
    maps = []

    for line in lines:
        maps.append([[[int(c) for c in b.split()] for b in a][0] for a in line[1:]])

    for i, m in enumerate(maps):
        maps[i] = sorted(m, key=lambda x: x[1])

    transformers = []

    for i, m in enumerate(maps):
        rules = []
        for end, start, length in m:
            rules.append([start, start + length - 1, end - start])
        transformers.append(rules)

    stack = seeds

    for transformer in transformers:
        new = []

        while stack:
            s = stack.pop()
            ss, se = s
            for i, t in enumerate(transformer):
                [ts, te, tval] = t
                if ss > te:
                    if i == len(transformer) - 1:
                        new.append(s)
                
                    continue
                elif se < ts:

                    new.append(s)
                    break
                else:

                    transformed, backToStack = splitOrReturn(s, t)
                    new.append(transformed)
                    if backToStack:
                        for bts in backToStack:
                            stack.append(bts)
                    break

        stack = new
    return sorted(stack, key=lambda x: x[0])[0][0]


fn = "2023/resources/input_05.txt"
fnt = "2023/resources/test.txt"

print(f"pt1: {main(fn)}\n" f"pt2: {part2(fn)}")