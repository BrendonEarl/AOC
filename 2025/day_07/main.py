
class Node:
    def __init__(self, coord):
        self.coord = coord
        self.used = False
        self.left = None
        self.right = None
        self.coefficient = 1

    def __repr__(self):
        return ' o '

    def use(self):
        self.used = True

    def isUsed(self):
        return self.used

    def quantumSplit(self):
        self.coefficient += 1

def main(filename, pt2=True):

    with (f:=open(filename)):
        lines = [[y for y in x.strip()] for x in f.readlines()]
    f.close()

    nrows, ncols = len(lines), len(lines[0])
    start = 0
    for i in range(ncols):
        if lines[0][i]=='S':
            start = i
            lines[0][i] = '.'

    for j in range(nrows):
        if lines[j][start] == '^':
            startNode = Node((j,start))
            lines[j][start] = startNode
            break
    for r in range(nrows):
        for c in range(ncols):
            if lines[r][c] == '^':
                lines[r][c] = Node((r,c))

    doSplit(startNode,lines, (startNode.coord[0],startNode.coord[1]-1), True)
    doSplit(startNode,lines, (startNode.coord[0],startNode.coord[1]+1), False)

    answer = doAdd2(startNode) if pt2 else doAdd(startNode)
    return answer
def doAdd(node):
    if node is None:
        return 0
    return 1 + doAdd(node.left) + doAdd(node.right)
def doAdd2(node):
    if node is None:
        return 0
    # if node.left is not None:
    #     node.left.coefficient *= (node.coefficient//2)
    # if node.right is not None:
    #     node.right.coefficient *= (node.coefficient//2)
    return node.coefficient + (doAdd2(node.left) + doAdd2(node.right))
def isNode(thing):
    return type(thing)==Node
def doSplit(node, lines, coord, isleft):

    r,c = coord
    if r > len(lines)-1:
        if isleft:
            node.left = None
        else:
            node.right = None
        return
    if isNode(n:=lines[r][c]):
        if not n.isUsed():
            n.use()
            if isleft:
                node.left = n
            else:
                node.right = n

            doSplit(n, lines, (n.coord[0], n.coord[1] - 1), True)
            doSplit(n, lines, (n.coord[0], n.coord[1] + 1), False)
        n.quantumSplit()
        return
    doSplit(node,lines,(coord[0]+1,coord[1]), isleft)

filename = '../resources/input_07.txt'
filename = '../resources/test_07.txt'

print(f'pt1: {main(filename, False)} \n'
      f'pt2: {main(filename)}')
