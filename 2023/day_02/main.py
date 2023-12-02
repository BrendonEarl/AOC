from math import prod


maxx = {
    'red':12,
    'green':13,
    'blue':14,
}

def isValid(vars):
    num,color = vars
    return (int(num) <= maxx[color])

def minDice(game):
    maxColor = {
        'red' : 0,
        'green' : 0,
        'blue' : 0,
    }
    
    for round in game:
        for num,color in round:
            maxColor[color] = max(int(num),maxColor[color])
    return prod(list(maxColor.values()))

def main(filename, pt2 = True):
    sum, games = 0, [line.strip().split(':') for line in open(filename)]

    for id,game in games:
        id = int(id.strip('Game '))
        game = game.split(';')

        if(pt2):
            sum += minDice([[y.strip().split(' ') for y in x.strip().split(',')] for x in game])
        else:
            sum += id if all([all([ isValid(y.strip().split(' ')) for y in x.strip().split(',')]) for x in game]) else 0

    return sum

fn = '2023/resources/input_02.txt'
fnt = '2023/resources/test.txt'

print(f'pt1: {main(fn, False)} \n'
      f'pt2: {main(fn)}')