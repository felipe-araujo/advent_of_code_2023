import sys
from textwrap import dedent

def split_numbers(line: str):
    return set(map(int, line.strip().split()))

def compute_points(line: str):
    matches = compute_matches(line)
    if matches == 0:
        return 0
    else:
        return 2**(matches-1)

def compute_matches(line: str):
    _card_n, line = line.split(':')
    winning, my_numbers = map(split_numbers, line.split('|'))
    return len(winning.intersection(my_numbers))

def part_01():
    total = 0
    with open('04_input.txt') as f:
        total = sum([compute_points(line) for line in f.readlines()])
    return total

def part_02():
    with open('04_input.txt') as f:
        return compute_part_02(f.readlines())

def compute_part_02(lines):
    points = []
    for line in lines:
        points.append(compute_matches(line))
    cards = [1 for i in range(0, len(points))]
    for i, p in enumerate(points):
        for k in range(i+1, i+p+1):
            if k < len(cards):
                cards[k] += cards[i]
    return sum(cards)

def main():
    print('Part 01:', part_01())
    print('Part 02:', part_02())
    

def run_test():
    # Tests for part 02
    example = \
        """
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
        """
    example = dedent(example).strip()
    print(example)
    example = example.split('\n')
    result = compute_part_02(example)
    assert 4 == compute_matches(example[0]), 'got ' + str(compute_points(example[0]))
    assert 30 == result, 'expected 30 but got ' + str(result)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        run_test()
    else:
        main()