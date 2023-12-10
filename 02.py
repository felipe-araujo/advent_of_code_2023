from dataclasses import dataclass, field
import sys

@dataclass
class Game:
    id: int
    sets: field(default_factory=list)

@dataclass
class Sets:
    red: int = 0
    green: int = 0
    blue: int = 0


def parse(line: str):
    id, plays = line.split(':')
    id = int(id.replace('Game', '').strip())
    g = Game(id, sets=[])
    for play in plays.split(';'):
        s = Sets(0, 0, 0)
        for occurence in play.split(','):
            value, key = occurence.split()
            setattr(s, key.strip(), int(value.strip()))
        g.sets.append(s)
    return g

def is_possible(g: Game, red: int, green: int, blue: int):
    return max(map(lambda s: s.red, g.sets)) <= red and\
        max(map(lambda s: s.green, g.sets)) <= green and\
        max(map(lambda s: s.blue, g.sets)) <= blue

def power_of_minimum(g: Game):
    return max(map(lambda s: s.red, g.sets)) * \
        max(map(lambda s: s.green, g.sets)) * \
        max(map(lambda s: s.blue, g.sets))

def main():
    with open('02_input.txt') as f:
        games = list(map(lambda x: parse(x), f.readlines()))
        answer1 = sum([g.id for g in games if is_possible(g, 12, 13, 14)])
        answer2 = sum([power_of_minimum(g) for g in games])
    print(answer1)
    print(answer2)

def run_test():
    g = parse('Game 8: 4 red, 6 green, 4 blue; 4 red, 1 green; 9 blue, 1 green, 11 red')
    assert g.id == 8
    assert len(g.sets) == 3
    print(g)
    assert True == is_possible(g, 11, 6, 9)
    assert False == is_possible(g, 3, 3, 3)

    # 12 red cubes, 13 green cubes, and 14 blue cubes
    g = parse('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert True == is_possible(g, 12, 13, 14)

    g = parse('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
    assert False == is_possible(g, 12, 13, 14)

    g = parse('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert 48 == power_of_minimum(g), 'computed value is ' + str(power_of_minimum(g))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        run_test()
    else:
        main()