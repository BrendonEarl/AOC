def findSimilarChars(line):
    first, last = line[:int(len(line) / 2)], line[int(len(line) / 2):]
    for char in first:
        if char in last:
            return char
    return None


def getSimilarCharsInGroup(group):
    first, second, third = group
    for char in first:
        if (char in second) and (char in third):
            return char
    return None


def main(filename):
    arr = [line.strip() for line in open(filename).readlines()]

    get_priority = lambda char: ord(char) - 96 if ord(char) > 90 else ord(char) - 38
    get_group = lambda num, array: [array[(i * 3)], array[(i * 3) + 1], array[(i * 3) + 2]]

    total_priorities, group_badge_total = 0, 0

    for line in arr:
        total_priorities += get_priority(findSimilarChars(line))
    for i in range(int(len(arr) / 3)):
        group_badge_total += get_priority(getSimilarCharsInGroup(get_group(i, arr)))

    print(f'part1: {total_priorities} \n'
          f'part2: {group_badge_total}')



main('resources/input_3.txt')