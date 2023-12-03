import numpy as np

def main(filename):
    sum, lines = 0, [[y for y in line.strip()] for line in open(filename)]
    maxLine, min = len(lines), 0
    for lineID, data in enumerate(lines:=[x for x in lines]):
        queue = []
        maxData = len(data)
        for id, char in enumerate(data):
            # print(f'{id}: {char}')
            if(queue and queue.pop()):
                continue
            if(char.isnumeric()):
                maxID = id + 1
                while(maxID<maxData and data[maxID].isnumeric()):
                    queue.append(True)
                    maxID += 1
                ll,bl,li,bi = lineID-1 if lineID>min else lineID, lineID+1 if lineID<maxLine else lineID, id-1 if id>min else id, maxID+1 if id<maxData else id
                
                test = [line[li:bi] for line in lines[ll:bl+1]]
                flag = False
                for line in test:
                    if flag: break
                    for char in line:
                        if(char != '.' and not char.isnumeric()):
                            flag = True
                            break
                if(flag):
                    sum += int(''.join(data[id:maxID]))
    print(sum)

def part2(filename):
    sum, lines = 0, [[y for y in line.strip()] for line in open(filename)]
    maxLine, min = len(lines), 0
    for lineID, data in enumerate(lines:=[x for x in lines]):
        queue = []
        maxData = len(data)
        for id, char in enumerate(data):
            # print(f'{id}: {char}')
            if(queue and queue.pop()):
                continue
            if(char.isnumeric()):
                maxID = id + 1
                while(maxID<maxData and data[maxID].isnumeric()):
                    queue.append(True)
                    maxID += 1
                ll,bl,li,bi = lineID-1 if lineID>min else lineID, lineID+1 if lineID<maxLine else lineID, id-1 if id>min else id, maxID+1 if id<maxData else id
                
                test = [line[li:bi] for line in lines[ll:bl+1]]
                flag = False
                for line in test:
                    if flag: break
                    for char in line:
                        if(char != '.' and not char.isnumeric()):
                            flag = True
                            break
                if(flag):
                    sum += int(''.join(data[id:maxID]))
    print(sum)

fn = '2023/resources/input_03.txt'
fnt = '2023/resources/test.txt'

part2(fnt)