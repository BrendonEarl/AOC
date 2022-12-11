import operator
import math
import bisect

class Monkey():

    def __init__(self,id, items, operation, test) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test, self.ifTrue, self.ifFalse = test
        self.inspectCount = 0

    def __repr__(self) -> str:
        return f'{self.id}: {self.items} \n\t {self.operation} \n\t\t {self.test}--{self.ifTrue}:{self.ifFalse}'
    
    def operate(self):
        if not self.items: return None
        trueItems = []
        falseItems = []
        while self.items:
            inspect = self.items.pop(0)
            inspect = self.operation[0](inspect,self.operation[1] if str(self.operation[1]).isnumeric() else inspect)
            inspect = int((inspect-inspect%3)/3)
            if inspect%self.test == 0:
                trueItems.append(inspect)
            else:
                falseItems.append(inspect)
            self.inspectCount += 1
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
    
    for round in range(20):
        # print('----------------------------------------')
        
        for monkey in monkeys:
            ch = monkey.operate()
            if ch:
                tr, fl = ch
                if tr[1]:
                    [monkeys[tr[0]].items.append(item) for item in tr[1]]
                    
                if fl[1]:
                    [monkeys[fl[0]].items.append(item) for item in fl[1]]

        #     print(ch)
        # for monkey in monkeys:
        #     print(monkey)
        print(round)

    highest = []
    for monkey in monkeys:
        bisect.insort(highest,monkey.inspectCount)
    
    print(math.prod(highest[-2:]))

        

test = 'resources/input_11_test.txt'
test1 = 'resources/input_11.txt'
main(test1)
