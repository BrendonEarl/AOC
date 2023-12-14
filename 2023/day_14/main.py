import numpy as np


def main(fn, pt2 = True):
    with open(fn) as f:
        lines = [[*line.strip()] for line in f]
        lines = np.array(lines)
        
    f.close()


    mr, mc = lines.shape
    stress = []
    
    if pt2:
        for z in range(1, 1000000001):
            t = 0
            for k, row in enumerate(lines):
                t += (mr - k) * sum([(1 if v=='O' else 0) for v in row]) 
            stress.append(t)
            
            if not z % 100:
                break
                
            #north
            cols = lines.T
            for i in range(mc):
                for j in range(mr):
                    if cols[i][j] == 'O':
                        
                        jplace = j
                        nxt = j-1
                        while (nxt >=0) and (cols[i][nxt] == '.'):
                            jplace -= 1
                            nxt -= 1
                        lines[j][i] = '.'
                        lines[jplace][i] = 'O'
            # print(lines)
            #west
            for i in range(mr):
                for j in range(mc):
                    if lines[i][j] == 'O':
                        
                        jplace = j
                        nxt = j-1
                        while (nxt >=0) and (lines[i][nxt] == '.'):
                            jplace -= 1
                            nxt -= 1
                        lines[i][j] = '.'
                        lines[i][jplace] = 'O'
            # print(lines)
            
            #south
            cols = lines.T
            for i in range(mc-1,-1,-1):
                for j in range(mr-1,-1,-1):
                    if cols[i][j] == 'O':
                        
                        jplace = j
                        nxt = j+1
                        while (nxt < mr) and (cols[i][nxt] == '.'):
                            jplace += 1
                            nxt += 1
                        lines[j][i] = '.'
                        lines[jplace][i] = 'O'
            
            # print(lines)

            #west
            for i in range(mr-1,-1,-1):
                for j in range(mc-1,-1,-1):
                    if lines[i][j] == 'O':
                        
                        jplace = j
                        nxt = j+1
                        while (nxt < mc) and (lines[i][nxt] == '.'):
                            jplace += 1
                            nxt += 1
                        lines[i][j] = '.'
                        lines[i][jplace] = 'O'
            # print(lines)
            
        return stress
    else:
        stress = 0
        cols = lines.T
        for i in range(mc):
            for j in range(mr):
                if cols[i][j] == 'O':
                    
                    jplace = j
                    nxt = j-1
                    while (nxt >=0) and (cols[i][nxt] == '.'):
                        jplace -= 1
                        nxt -= 1
                    lines[j][i] = '.'
                    lines[jplace][i] = 'O'
            
    

        for k, row in enumerate(lines):
            stress += (mr - k) * sum([(1 if v=='O' else 0) for v in row])
        return stress
    


fn = '2023/resources/input_14.txt'
fnt = '2023/resources/test14.txt'

print(f"pt1: {main(fn,False)}") #\npt2: {main(fn)}")