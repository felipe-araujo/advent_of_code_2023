import sys
from textwrap import dedent
from dataclasses import dataclass, field

@dataclass
class Number:
    value: int
    start: int
    end: int
    line_num: int

def is_digit(t: str):
    return ord(t) >= ord('0') and ord(t) <= ord('9')

def is_symbol(t: str):
    return not is_digit(t) and t != '.'

def read_numbers(line: str, line_num: int):
    acc = []
    i = 0
    while i < len(line):
        start = i
        acc = []
        while i<len(line) and is_digit(line[i]):
            acc.append(line[i])
            i +=1
        if len(acc) > 0:
            val = int(''.join(acc))
            yield Number(val, start, i, line_num)
        else:
            i += 1

def has_adjacent_symbol(n: Number, matrix: list[str]):
    print(n)

    line_size = len(matrix[n.line_num])
    print(line_size)
    # same line
    if n.start > 0 and is_symbol(matrix[n.line_num][n.start-1]):
        return True
    if n.end < line_size and is_symbol(matrix[n.line_num][n.end]):
        return True
    
    # one line below
    if n.line_num+1 < len(matrix):
        for i in range(n.start, n.end):
            if is_symbol(matrix[n.line_num+1][i]):
                return True
        if n.start > 0 and is_symbol(matrix[n.line_num+1][n.start-1]):
            return True
        if n.end < line_size and is_symbol(matrix[n.line_num+1][n.end]):
            return True
    
    # one line above
    if n.line_num > 0:
        for i in range(n.start, n.end):
            if is_symbol(matrix[n.line_num-1][i]):
                return True
        if n.start > 0 and is_symbol(matrix[n.line_num-1][n.start-1]):
            return True
        if n.end < line_size and is_symbol(matrix[n.line_num-1][n.end]):
            return True
    return False

def compute_total(matrix):
    total = 0
    for i, line in enumerate(matrix):
        total += sum([n.value for n in read_numbers(line, i) if has_adjacent_symbol(n, matrix)])
    return total

def main():
    total = 0
    with open('03_input.txt') as f:
        matrix = list(map(lambda line: list(line), f.readlines()))
        total = compute_total(matrix)
    print(total)
    assert not int(total) >= 537811
    

def run_test():
    example = """
                467..114..
                ...*......
                ..35..633.
                ......#...
                617*......
                .....+.58.
                ..592.....
                ......755.
                ...$.*....
                .664.598..
                """
    example = dedent(example).strip()
    print(example)
    example = list(map((lambda line: list(line.strip())), example.split('\n')))
    for l in example:
        print(l)
    assert compute_total(example) == 4361

    for d in ['$', '/', '*', '@', '-', '=', '%']:
        assert is_symbol(d), "not a symbol? " + d

    
    sample = [list('664.-&==4.5*.98..9%')]
    numbers = list(read_numbers(sample[0], 0))
    print(numbers)
    assert not has_adjacent_symbol(numbers[0], sample)
    assert has_adjacent_symbol(numbers[1], sample)
    assert has_adjacent_symbol(numbers[2], sample)
    assert not has_adjacent_symbol(numbers[3], sample)
    assert has_adjacent_symbol(numbers[4], sample)

    sample = [list('*...'), list('12.3'), list('8.45'),list('1.4.'), list('...$')]
    numbers = list(read_numbers(sample[1], 1))
    print(numbers)
    assert has_adjacent_symbol(numbers[0], sample)
    assert not has_adjacent_symbol(numbers[1], sample)
    numbers = list(read_numbers(sample[2], 2))
    assert not has_adjacent_symbol(numbers[0], sample)
    assert not has_adjacent_symbol(numbers[1], sample)

    numbers = list(read_numbers(sample[3], 3))
    assert not has_adjacent_symbol(numbers[0], sample)
    assert has_adjacent_symbol(numbers[1], sample)

    total = compute_total(sample)
    assert total == (12+4)

    naturals = list(read_numbers('1.2&.?3', 0))
    print(naturals)
    assert len(naturals) == 3
    assert naturals[0].value == 1
    assert naturals[0].start == 0
    assert naturals[0].end == 1
    total = compute_total(list('1.2&.?3'))
    assert total == (2+3), 'returned value was ' + str(total) 
    

    # check adjencies in the same line
    fifth_line = example[4]
    numbers = list(read_numbers(fifth_line, 4))
    print(numbers[0])
    assert has_adjacent_symbol(numbers[0], example)

    # check adjencies above, below and in diagonal
    third_line = example[2]
    numbers = list(read_numbers(third_line, 2))
    print(numbers[0])
    assert has_adjacent_symbol(numbers[0], example)

    # numbers that do not have adjacent symbols
    first_line = example[0]
    numbers = list(read_numbers(first_line, 0))
    print(numbers[1])
    assert numbers[1].value == 114, 'expected 114 but got ' + str(numbers[1].value)
    assert not has_adjacent_symbol(numbers[1], example)

    sixth_line = example[5]
    numbers = list(read_numbers(sixth_line, 5))
    print(numbers[0])
    assert numbers[0].value == 58
    assert not has_adjacent_symbol(numbers[0], example)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        run_test()
    else:
        main()