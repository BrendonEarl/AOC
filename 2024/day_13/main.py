
def day_13(fn, pt1=True):
    with open(fn) as f:
        lines = [block.split('\n') for block in f.read().split('\n\n')]
    f.close()

    totcoins = 0
    for A,B,P in lines:

        xa,ya = [int(j.split('+')[1]) for j in A.split(':')[1].strip().split(',')]
        xb,yb = [int(j.split('+')[1]) for j in B.split(':')[1].strip().split(',')]
        xt,yt = [int(j.split('=')[1]) for j in P.split(':')[1].strip().split(',')]
        xt,yt = (xt,yt) if pt1 else (xt + 10000000000000, yt + 10000000000000)

        numa = (xb * yt) - (yb * xt)
        numb = (xa * yt) - (ya * xt)

        dena = (xb * ya) - (xa * yb)
        denb = (xa * yb) - (ya * xb)


        if not (((numa <= 0 and dena < 0) or (numa >=0 and dena > 0)) and ((numb <= 0 and denb < 0) or (numb >=0 and denb > 0))):
            continue

        if numa%dena or numb%denb:
            continue

        a, b = int(numa/dena), int(numb/denb)
        totcoins += (3 * a) + b

    return totcoins

filename = '../resources/input_13.txt'
print(f"pt1: {day_13(filename)}\n"
      f"pt2: {day_13(filename, False)}")
