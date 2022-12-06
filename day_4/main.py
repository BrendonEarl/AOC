def main(filename):
    arr = [line.strip().split(",") for line in open(filename).readlines()]
    is_contained = lambda one, two: \
        (one[0] >= two[0] and one[1] <= two[1]) or \
        (one[0] <= two[0] and one[1] >= two[1])
    is_overlapping = lambda one, two: \
        (one[0] in range(two[0], two[1] + 1) or
         one[1] in range(two[0], two[1] + 1)) or \
        (two[0] in range(one[0], one[1] + 1) or
         two[1] in range(one[0], one[1] + 1))

    totalcontained, totaloverlapping= 0, 0
    for line in arr:
        first, second = [int(num) for num in line[0].split("-")], [int(num) for num in line[1].split("-")]
        totaloverlapping += 1 if is_overlapping(first,second) else 0
        totalcontained += 1 if is_contained(first,second) else 0

    print(f'{totalcontained} \n'
          f'{totaloverlapping}')


main('resources/input_4.txt')