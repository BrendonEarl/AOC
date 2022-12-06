rules = {
    'AX' : 3,
    'AY' : 6,
    'AZ' : 0,
    'BX' : 0,
    'BY' : 3,
    'BZ' : 6,
    'CX' : 6,
    'CY' : 0,
    'CZ' : 3,
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}
revised = {
    'AX' : 3,
    'AY' : 1,
    'AZ' : 2,
    'BX' : 1,
    'BY' : 2,
    'BZ' : 3,
    'CX' : 2,
    'CY' : 3,
    'CZ' : 1,
    'X' : 0,
    'Y' : 3,
    'Z' : 6
}

def play_bout(bout, part2):
    opp, me = bout[0]+bout[1], bout[1]
    rule_book = revised if part2 else rules

    return rule_book[me] + rule_book[opp]


def play_game(strategy_guide, part2 = False):
    points = 0
    for bout in strategy_guide:
        points += play_bout(bout, part2)
    return points


def main(filename):
    strategy_guide = [line.strip().split() for line in open(filename).readlines()]
    print(f'original: {play_game(strategy_guide)} \n revised: {play_game(strategy_guide,True)}')


main('resources/input_2.txt')