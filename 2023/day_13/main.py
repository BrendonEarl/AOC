import numpy as np


def main(fn, pt2 = True):
    with open(fn) as f:
        lines = [[[*ch] for ch in line.split('\n')] for line in f.read().split('\n\n')]
    f.close()
    
    totRows,totCols = 0,0

    if pt2:
        
        for line in lines:
            pattern = np.array([*line])
            
            mr = pattern.shape[0]
            mc = pattern.shape[1]
            smudge = False
            found_flag = False
            for i in range(mr-1):
                if found_flag: break
                l,r = i, i+1
                rows = 0

                break_flag = False
                while (l >= 0 and r<mr) and (any(t:=[(pattern[l][i]==v) for i,v in enumerate(pattern[r])])):
                    cnt = t.count(False)
                    if (cnt > 1):
                        break
                    elif(cnt == 1):
                        if(not smudge):
                            smudge = True
                        else:
                            break_flag = True
                            break
                            
                    if break_flag: break
                    rows += 1
                    l,r = l-1,r+1
                
                if (l == -1 or r == mr) and smudge:
                    totRows += i+1
                    found_flag = True
                    
                else:
                    smudge = False

            
            smudge = False
            cpattern = pattern.T
            for i in range(mc-1):
                if found_flag: break
                l,r = i, i+1
                cols = 0
                break_flag = False
                while (l >= 0 and r<mc) and (any(t:=[(cpattern[l][i]==v) for i,v in enumerate(cpattern[r])])):
                    cnt = t.count(False)
                    if (cnt > 1):
                        break
                    elif(cnt == 1):
                        if(not smudge):
                            smudge = True
                        else:
                            break_flag = True
                            break
                    
                    if break_flag: break
                    cols += 1
                    l,r = l-1,r+1
                
                if (l == -1 or r == mc) and smudge:
                    totCols += i+1
                    found_flag = True
                    
                elif smudge:
                    smudge = False
        
    else:

        for line in lines:
            pattern = np.array([*line])
            
            break_flag = False
            mx = pattern.shape[0]
            for i in range(mx-1):
                if break_flag: break
                l,r = i, i+1
                rows = 0
                while (l >= 0 and r<mx) and (all([(pattern[l][i]==v) for i,v in enumerate(pattern[r])])):
                    rows += 1
                    l,r = l-1,r+1
                
                if (l == -1 or r == mx):
                    break_flag = True
                    totRows += i+1

            mx = pattern.shape[1]
            cpattern = pattern.T
            for i in range(mx-1):
                if break_flag: break
                l,r = i, i+1
                cols = 0
                while (l >= 0 and r<mx) and ( all([(cpattern[l][i]==v) for i,v in enumerate(cpattern[r])])):
                    cols += 1
                    l,r = l-1,r+1
                
                if (l == -1 or r == mx):
                    break_flag = True
                    totCols += i+1
                    

    return (totRows*100) + totCols

fn = '2023/resources/input_13.txt'
fnt = '2023/resources/test13.txt'

print(f"pt1: {main(fn, False)}\npt2: {main(fn)}")