
def day_07(fn, pt1=True):
    with open(fn) as f:
        equations = [line.strip().split(':') for line in f.readlines()]
        for i in range(len(equations)):
            equations[i][0]  = int(equations[i][0])
            equations[i][1] = [int(n) for n in equations[i][1].strip().split()]
    f.close()

    ans = 0
    if pt1:
        for sm,nums in equations:
            operators = [0 for _ in range(len(nums)-1)]
            bf = False
            while not all(operators):
                check = nums[0]
                for j in range(len(nums)-1):
                    check = check+nums[j+1] if operators[j] else check * nums[j+1]

                if check==sm:
                    ans+=sm
                    bf = True
                    break
                incr = True
                for i in range(len(operators)-1,-1,-1):
                    if incr and operators[i]:
                        operators[i]=0
                        incr = True
                    elif incr:
                        operators[i]=1
                        incr=False
            if not bf and sum(nums)==sm:
                ans+=sm
        return ans
    else:
        for sm,nums in equations:
            operators = [2 for _ in range(len(nums)-1)]
            bf = False
            while any(operators):
                check = nums[0]
                for j in range(len(nums)-1):
                    if operators[j] ==2:
                        check *= nums[j+1]
                    elif operators[j]==1:
                        check = int(str(check) + str(nums[j+1]))
                    else:
                        check += nums[j+1]

                if check==sm:
                    ans+=sm
                    bf = True
                    break

                decr = True
                for i in range(len(operators)-1,-1,-1):
                    if decr and operators[i]:
                        operators[i]-=1
                        decr=False
                    elif decr:
                        operators[i]=2
                        decr=True

            if not bf and sum(nums)==sm:
                ans+=sm
        return ans

filename = '../resources/input_07.txt'
t = '../resources/test_07.txt'
print(f"pt1: {day_07(filename)}\n"
      f"pt2: {day_07(filename,False)}")