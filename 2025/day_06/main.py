import math

def main(filename, pt2=True):

    if pt2:
        with (f := open(filename)):
            lines = f.read().split('\n')
        f.close()
        answer = 0

        x = max(len(line) for line in lines)
        for i in range(len(lines)):
            copy = lines[i]
            while len(copy) < x:
                copy += ' '
            lines[i] = copy[::-1]

        stack = []
        for i in range(len(lines[0])):
            toStack = ''
            for j in range(len(lines)):
                check = lines[j][i]
                if j < len(lines)-1:
                    toStack += check
                else:
                    stack.append(toStack)
                    if check != ' ':
                        stack.append(check)
        stack = stack[::-1]
        temp = []
        while len(stack)>0:
            test = stack.pop()
            if test.isspace(): continue
            test = test.strip()
            if test.isnumeric():
                temp.append(int(test))
            else:
                func = sum if test == '+' else math.prod
                answer += func(temp)
                temp.clear()
        return answer

    else:
        with (f:=open(filename)):
            lines = [[(int(y) if y.isnumeric() else y) for y in x.strip().split()] for x in f.readlines()]
            lines,operations = lines[:-1], lines[-1]
        f.close()

        answer = 0
        for i in range(len(lines[0])):
            func = sum if operations[i] == '+' else math.prod
            answer += func(line[i] for line in lines)

        return answer


filename = '../resources/input_06.txt'
# filename = '../resources/test_06.txt'

print(f'pt1: {main(filename, False)} \n'
      f'pt2: {main(filename)}')

# main(filename)