def main(fn, pt1 = False):
    with open(fn) as f:
        lines = [[int(x) for x in line.strip().split()] for line in f]
    f.close()

    s = 0
    for line in lines:
        tmp = [line]

        test = line
        while test and any(test):
            t = []
            for i in range(1,len(test)):
                t.append(test[i]-test[i-1])
            test = t
            tmp.append(t)
        
        ts = 0
        if pt1:
            for x in tmp[-1::-1]:
                ts = ts + x[-1]
        else:
            for i,x in enumerate(z:=tmp[-1::-1]):
                if i==0 : continue
                ts = (x[0] - ts)
        
        s += ts
    return s
                

fn = '2023/resources/input_09.txt'
fnt = '2023/resources/test9.txt'

print(f'pt1: {main(fn,True)} \npt2: {main(fn)}')