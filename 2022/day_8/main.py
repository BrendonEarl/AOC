import numpy as np

def main(filename):
    forest = np.array([[int(character) for character in line.strip()] for line in open(filename,encoding="UTF-8").readlines()],dtype=int)
    prob1 , prob2 = 0, 0
    numrows, numcols = forest.shape
    is_visible = lambda h, br,bc,ar,ac : h > max(br) or h > max(bc) or h > max(ar) or h > max(ac)
    for row, rowOfTrees in enumerate(forest):
        for col, tree_height in enumerate(rowOfTrees):
            rowTreesBefore =  forest[row,:][:col]
            rowTreesAfter = forest[row,:][col+1:] 
            colTreesBefore = forest[:,col][:row]
            colTreesAfter = forest[:,col][row+1:]
            temp_scenic_score = []
            if (row==0 or col == 0 or row+1==numrows or col+1==numcols):
                prob1 += 1
                continue
            else:
                prob1 += 1 if is_visible(tree_height, rowTreesBefore, colTreesBefore, rowTreesAfter, colTreesAfter) else 0
                    
            for lineOfTrees in [rowTreesBefore[-1::-1], rowTreesAfter, colTreesBefore[-1::-1], colTreesAfter]:
                visible_trees_in_line = 0
                for tree in lineOfTrees:
                    visible_trees_in_line += 1
                    if tree >= tree_height: break                    
                temp_scenic_score.append(visible_trees_in_line)
            
            prob2 = temp_scenic_score if (temp_scenic_score := np.prod(temp_scenic_score)) > prob2 else prob2
                 
    print(f' problem 1: {prob1} \n'
          f' problem 2: {prob2}')

main('resources/input_8.txt')