import re

regex = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

f = open('input')

lines = f.readlines()
total = 0

mapping = {
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

def get_number_from_str(number: str):
    try:
        int(number)
    except ValueError:
        return mapping[number]
    return number



def get_line_total(line_str: str):
    matches = re.finditer(regex, line_str)
    matches = list(matches)

    if len(matches) == 0:
        return 0
    first_number = matches[0].group(1)
    first_number = get_number_from_str(first_number)
    if len(matches) == 1:
        return int(first_number + first_number)
    last_number = matches[-1].group(1)
    last_number = get_number_from_str(last_number)
    return int(first_number + last_number)



for line in lines:
    total += get_line_total(line)

print(total)