algarisms = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}

def is_number(d):
    return ord(d) >= ord('0') and ord(d) <= ord('9')

def replace_with_number(line):
    i = 0
    numbers = []
    for i in range(0, len(line)):
        if(is_number(line[i])):
            numbers.append(int(line[i]))
        else:
            number = list(filter(lambda n: line[i:].startswith(n), algarisms))
            if len(number)>0:
                numbers.append(algarisms[number[0]])
    return numbers

def main():
    sum = 0
    with open('01_input.txt') as f:
        for line in f.readlines():
            digits = replace_with_number(line)
            sum = sum + digits[0] * 10 + digits[-1]
    print(sum)

def test():
    for s in ['two1nine', '4nineeightseven2', 'eightwothree']:
        print(s, ' -> ', replace_with_number(s))

if __name__ == "__main__":
    main()
    #test()