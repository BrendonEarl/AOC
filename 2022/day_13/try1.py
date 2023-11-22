def yes(left,right):
    print(f'\t{left} : {right} is in order')
    return 1

def no(left, right):
    print(f'\t{left} : {right} is not in order')
    return 0


def isInOrder(packet:list)-> bool : 
    left,right = packet
    return IIO(left,right)


def IIO(left,right,spacing=''):
    
    print(f'{spacing}{left} : {right}',end='\n\n')
    if type(left)==int:
        if type(right)==int:
            if left<right: return yes(left,right)
            if right<left: return no(left,right)
            return 'same'
        elif not right:
            return no(left,right)
        elif type(right) == list:
            left = [left]
    elif type(right) == int:
        if not left:
            return no(left,right)
        elif type(left)==list:
            right = [right]
        

    for _ in range(len(left)):
        if (left and not right):
            return no(left,right)
        if (right and not left):
            return yes(left,right)
        if (not left and not right):
            return yes(left,right)
        
        if _ >= len(right): return no(left,right)
        l,r = left[_], right[_]
        # print(f'{spacing}{l}:{r}')
        if (a:=IIO(l,r,spacing+'  ')) != 'same':
            return a
    
    
    if len(right) > len(left):
        return yes(left,right)
       
    
    return 'same'

def main(filename):
    packets = [[eval(halfpacket) for halfpacket in packet.strip().split('\n')] for packet in open(filename).read().split('\n\n')]
    # [print(packet, end='\n\n') for packet in packets]

    indices = []

    for index, packet in enumerate(packets):
        pass

    tot = [(numInorder:=0)+ isInOrder(packet) for packet in packets]
    answer = 0
    print(tot)
    for index,val in enumerate(tot):
        if val:
            answer+= index+1
    print(answer)

test = 'resources/input_13_test.txt'
real = 'resources/input_13.txt'

main(real)