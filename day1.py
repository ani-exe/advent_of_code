import re

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('input.txt', 'r') as f:
    ls = [line.strip() for line in f]

all = []
for line in ls:
    pattern = re.compile(r'(' + '|'.join(numbers.keys()) + r')')
    newline = re.sub(pattern, lambda x: numbers[x.group()], line)
    m = re.findall('\d', newline)
    first = m[0]
    last = m[-1]
    print(line, first + last)
    all.append(int(first+last))

print(all)
print(sum(all))



