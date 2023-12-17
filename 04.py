import sys

def split_numbers(line: str):
    return set(map(int, line.strip().split()))

def compute_points(line: str):
    card_n, line = line.split(':')
    winning, my_numbers = map(split_numbers, line.split('|'))
    matches = len(winning.intersection(my_numbers))
    if matches == 0:
        return 0
    else:
        return 2**(matches-1)

def main():
    total = 0
    with open('04_input.txt') as f:
        total = sum([compute_points(line) for line in f.readlines()])
    print('Part 01:', total)

def run_test():
    pass

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        run_test()
    else:
        main()