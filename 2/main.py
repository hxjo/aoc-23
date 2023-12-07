import re

f = open('input')
lines = f.readlines()
regex = r'(\d+)\s*(\w+)'
# 12 red cubes, 13 green cubes, and 14 blue cubes?
MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}

total = 0

def process_line(line_str: str):
    game_id = int(line.split(':')[0].split('Game ')[1])
    input = line.split(':')[1]
    groups = input.split(';')
    max_game = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for group in groups:
        matches = re.findall(regex, group)
        for match in matches:
            (number, color) = match
            if int(number) > max_game[color]:
                max_game[color] = int(number)

    return max_game['red'] * max_game['blue'] * max_game['green']



for line in lines:
    total += process_line(line)

print(total)