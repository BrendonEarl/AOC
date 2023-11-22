import bisect

def getMostCalories(arr, problem1 = False):

    most_calories, temp_total = [], 0

    for i in arr:
        if i.isnumeric():
            temp_total += int(i)
        else:
            bisect.insort(most_calories, temp_total)
            temp_total = 0
    bisect.insort(most_calories, temp_total)

    return most_calories[-1] if problem1 else sum(most_calories[-1:-4:-1])


def main(filename):
    arr = [line.strip() for line in open(filename).readlines()]

    print(f' one elf: {getMostCalories(arr, True)} \n'
          f' top three elves : {getMostCalories(arr, False)}')

main('resources/input_1.txt')