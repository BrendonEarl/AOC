import operator
import math
import bisect
class Item():

    def __init__(self, val, owner) -> None:
        self.val = val
        self.owner = owner
        self.owners = [owner]
    
    def __repr__(self) -> str:
        return self.val
    
class Monkey():

    def __init__(self,id, items, operation, test) -> None:
        self.id = id
        self.items = [Item(item,id) for item in items]
        self.operation = operation
        self.test, self.ifTrue, self.ifFalse = test
        self.inspectCount = 0
        self.track = 0

    def __repr__(self) -> str:
        return f'{self.id}: {self.items} \n\t {self.operation} \n\t\t {self.test}--{self.ifTrue}:{self.ifFalse}'
    
    def operate(self):
        if not self.items: return None
        trueItems = []
        falseItems = []
        self.track = 0
        while self.items:
            inspect = self.items.pop(0)
            inspect.val = self.operation[0](inspect.val,self.operation[1] if str(self.operation[1]).isnumeric() else inspect.val)
            # inspect.val = int((inspect.val-inspect.val%3)/3)
            if inspect.val%self.test == 0:
                trueItems.append(inspect)
            else:
                falseItems.append(inspect)
            self.inspectCount += 1
            self.track += 1
        return [[self.ifTrue,trueItems],[self.ifFalse,falseItems]]

def main(filename):
    operations = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv,
    }
    arr = [[line.split() for line in monkey.split('\n')] for monkey in open(filename).read().split('\n\n')]

    # [print(line) for line in arr]
    monkeys = []
    # print(arr)
    for line in arr:
        monkeys.append(
            Monkey(
                id=int(line[0][1].strip(':')),
                items=[int(item.strip(',')) for item in line[1][2:]],
                operation=[operations[line[2][-2]], int(line[2][-1]) if line[2][-1].isnumeric() else line[2][-1]],
                test=[int(line[3][-1]),
                    int(line[4][-1]),
                    int(line[5][-1])]
            )
        )
    insp = []
    for monkey in monkeys:
        insp.append(monkey.track)
    for round in range(120):
        # print('----------------------------------------')
        
        for monkey in monkeys:
            ch = monkey.operate()
            insp[monkey.id] = monkey.track
            
            if ch:
                tr, fl = ch
                if tr[1]:
                    for item in tr[1]:
                        item.owners.append(tr[0])
                    [monkeys[tr[0]].items.append(item) for item in tr[1]]
                    
                if fl[1]:
                    for item in fl[1]:
                        item.owners.append(fl[0])
                    [monkeys[fl[0]].items.append(item) for item in fl[1]]
        print(insp[1],end=' ')
        #     print(ch)
        # for monkey in monkeys:
        #     print(monkey)
        # print()

    highest = []
    # for monkey in monkeys:
    #     for item in monkey.items:
    #         print(f' : {item.owners}')
    #         print('\n\n')
    #     bisect.insort(highest,monkey.inspectCount)
    
    # print(math.prod(highest[-2:]))

        

test = 'resources/input_11_test.txt'
test1 = 'resources/input_11.txt'
main(test1)
