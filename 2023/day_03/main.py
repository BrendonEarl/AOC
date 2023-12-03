from math import prod

def main(filename):
    sum, lines = 0, [[y for y in line.strip()] for line in open(filename)]
    maxLine, min = len(lines), 0
    for lineID, data in enumerate(lines:=[x for x in lines]):
        queue, maxData = [], len(data)

        for id, char in enumerate(data):
            if(queue and queue.pop()):
                continue

            if(char.isnumeric()):
                maxID = id + 1
                while(maxID<maxData and data[maxID].isnumeric()):
                    queue.append(True)
                    maxID += 1

                ll,bl,li,bi = lineID-1 if lineID>min else lineID, lineID+1 if lineID<maxLine else lineID, id-1 if id>min else id, maxID+1 if id<maxData else id
                test, flag = [line[li:bi] for line in lines[ll:bl+1]], False
                for line in test:
                    if flag: break
                    for char in line:
                        if(char != '.' and not char.isnumeric()):
                            flag = True
                            break
                sum += int(''.join(data[id:maxID])) if flag else 0
    return sum

def part2(filename):
    sum, lines = 0, [[y for y in line.strip()] for line in open(filename)]
    maxLine, min = len(lines), 0
    for lineID, data in enumerate(lines:=[x for x in lines]):
        maxData = len(data)
        for id, char in enumerate(data):
        
            if(char == '*'):
                maxID = id + 1
                
                ll,bl,li,bi = lineID-1 if lineID>min else lineID, lineID+1 if lineID<maxLine else lineID, id-1 if id>min else id, id+1 if id<maxData else id
                
                test = [line for line in lines[ll:bl+1]]
                n,nums = 0,[]
                for line in test:
                    queue = []
                    for i in range(li,bi+1):
                        if(queue and queue.pop()):
                            continue
                        if(line[i].isnumeric()):
                            n += 1
                            start,end = i,i
                            while(start-1 >= min and line[start-1].isnumeric()):
                                start-=1
                            while(end < maxData and line[end].isnumeric()):
                                end+=1
                                queue.append(True)
                            
                            nums.append(int(''.join(line[start:end])))
                sum += prod(nums) if n==2 else 0

    return sum

fn = '2023/resources/input_03.txt'
fnt = '2023/resources/test.txt'

print(f'pt1: {main(fn)}\n'
      f'pt2: {part2(fn)}')