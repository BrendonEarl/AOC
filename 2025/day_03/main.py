
def main(filename, pt1=True):
    with (f:=open(filename)):
        lines = [[int(y) for y in x.strip()] for x in f.readlines()]
    f.close()

    answer = 0

    if pt1:
        for line in lines:
            one, onedex = 0, 0
            two = 0

            for i, num in enumerate(line[:-1]):
                if num > one:
                    one = num
                    onedex = i

            for j, num in enumerate(line):
                if (j > onedex) and (num > two):
                    two = num
            answer += (10 * one) + two
    else:
        for line in lines:
            snum, prevdex, l = '', 0, len(line)

            for i in range(11,-1,-1):
                high = 0
                for j,num in enumerate(line):
                    if l-i > j and (j > prevdex or i==11) and num > high:
                        high = num
                        prevdex = j
                snum += str(high)
            answer += int(snum)
    return answer

filename = '../resources/input_03.txt'
print(f'pt1: {main(filename)} \n'
      f'pt2: {main(filename, False)}')