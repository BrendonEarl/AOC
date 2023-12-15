
def main(fn, pt1=True):
    with open(fn) as f:
        pieces = f.read().strip().split(',')
    f.close()

    hsh = lambda x,c: ((x + ord(c)) *17) % 256
    summ = 0
    if pt1:
        
        for piece in pieces:
            
            xval = 0
            for character in piece:
                xval = hsh(xval, character)
            summ += xval

        return summ
    else:
        boxes = {i : {} for i in range(256)}
        
        for piece in pieces:

            if piece[-1] == '-':
                string = piece[:-1]
                boxnum = 0
                for character in string:
                    boxnum = hsh(boxnum, character)
                try:
                    boxes[boxnum].pop(string)
                except KeyError:
                    pass
                
            else:
                string, lense = piece.split('=')

                boxnum = 0
                for character in string:
                    boxnum = hsh(boxnum, character)

                boxes[boxnum][string] = lense
        
        summ = 0
        for box, lenses in enumerate(boxes.values()):

            tsum = 0
            for i, l in enumerate(lenses.values()):
                tsum += (box+1) * (i+1) * int(l)
            summ += tsum
        return summ


fn = '2023/resources/input_15.txt'
fnt = '2023/resources/test15.txt'

print(f"pt1: {main(fn)} \npt2: {main(fn,False)}")