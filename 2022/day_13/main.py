def yes(left,right,spacing):
    # print(f'{spacing}{left} : {right} is in order')
    return 1

def no(left, right,spacing):
    # print(f'{spacing}{left} : {right} is not in order')
    return 0


def isInOrder(packet:list)-> bool :
    left,right = packet
    return IIO(left,right)


def IIO(left,right,spacing=''):
    # print(f'{spacing}{left} : {right}',end='\n\n')
    if type(left)== int and type(right) == int:
        if left<right: return yes(left,right,spacing + '  ')
        if right<left: return no(left,right,spacing + '  ')
        return 'same'

    elif type(left)== list and type(right) == list:

        for i,_ in enumerate(left):
            if (left and not right):
                return no(left,right,spacing + '  ')
            if (right and not left):
                return yes(left,right,spacing + '  ')
            if (not left and not right):
                return yes(left,right,spacing + '  ')

            if i >= len(right):
                return no(left,right,spacing + '  ')
            l,r = left[i], right[i]
            if (a:=IIO(l,r,spacing+'  ')) != 'same':
                return a

    else:
        if type(left)== int: left = [left]
        else: right = [right]
        if (a:=IIO(left,right,spacing+'  ')) != 'same':
            return a


    if len(right) > len(left):
        return yes(left,right,spacing + '  ')

    return 'same'

def main(filename):
    packets = [[eval(halfpacket) for halfpacket in packet.strip().split('\n')] for packet in open(filename).read().split('\n\n')]
    # [print(packet, end='\n\n') for packet in packets]

    indices = []

    for index, packet in enumerate(packets):
        pass

    tot = [(numInorder:=0)+ isInOrder(packet) for packet in packets]
    answer = 0
    
    for index,val in enumerate(tot):
        if val:
            answer+= index+1
    print(f'pt1 {answer}')

    two, six = [[2]], [[6]]
    twoindex, sixindex = 1, 2

    for packet in packets:
        for half in packet:
            if isInOrder([half,two]):
                twoindex, sixindex = twoindex+1,sixindex+1
            elif isInOrder([half,six]):
                sixindex += 1
    
    print(f'pt2 {twoindex},{sixindex} : {twoindex*sixindex}')


test = '2022/resources/input_13_test.txt'
real = '2022/resources/input_13.txt'

main(real)