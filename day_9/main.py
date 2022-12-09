def main(filename, part2=True):

    moves = [line.strip().split() for line in open(filename).readlines()]

    snake, visited, x, y, HEAD = [], [[0,0]], 0, 1, 0

    [snake.append([0,0]) for _ in range(10 if part2 else 2)]
    
    dirs = {
        'D' : [0,1],
        'U' : [0,-1],
        'R' : [1,0],
        'L' : [-1,0]
    }

    is_adjacent = lambda head, tail : abs(tail[x]-head[x]) <= 1 and abs(tail[y]-head[y]) <= 1

    getHead = lambda snake: snake[HEAD]
    moveHead = lambda snake, direction : [getHead(snake)[x] + dirs[direction][x], getHead(snake)[y] + dirs[direction][y]]

    for direction, distance in moves:
        for turn in range(distance := int(distance)):
            
            snake[HEAD] = moveHead(snake,direction)

            for index, tail in enumerate(snake[1:]):
                head = snake[index]
                headx, heady = head
                tailx, taily = tail
                
                if not is_adjacent(head,tail):
                    if(tailx == headx):
                        tail[y] += 1 if taily<heady else -1
                    elif(taily == heady):
                        tail[x] += 1 if tailx<headx else -1
                    else:
                        tail[y] += 1 if taily<heady else -1
                        tail[x] += 1 if tailx<headx else -1
                    
                    if index == len(snake)-2:
                        if snake[index+1] not in visited:
                            visited.append(snake[index+1].copy())
    return(len(visited))   

            
FILE_NAME = 'resources/input_9.txt'
print(f' problem 1: {main(FILE_NAME)} \n'
      f' problem 2: {main(FILE_NAME,False)}')