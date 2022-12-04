import logging



logging.basicConfig(filename='day3.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.info('Start of program')

def get_priority(character:str):
    if character.islower():
        return ord(character) - 96 # lower a-z is 1-26
    else:
        return ord(character) - 38 # upper A-Z is 27-52

with open('input.txt') as f:
    lines = f.read().splitlines()

priority_sums=0
halves = [(line[0:len(line)//2], line[len(line)//2:]) for line in lines]
for half in halves:
    one, two = half
    common_char = set(one).intersection(set(two)).pop() # assumes only one 
    # print(common_char)
    priority_sums += get_priority(common_char)

print(f'The sum of the priorities of the duplicates is {priority_sums}')
# print(f'The lines are divisible by 3? {len(lines)}/3 = {len(lines)/3}')

group_counter = 0
badge_sums = 0
while group_counter * 3 < len(lines):
    start = group_counter * 3
    group_counter += 1
    common_char = set(lines[start]).intersection(set(lines[start+1]), 
                                                 set(lines[start+2])).pop()
    badge_sums += get_priority(common_char)
    logging.debug(f'Group: {group_counter}, Badge: {common_char}')
    logging.debug(f'    {lines[start]}-> set: {sorted(set(lines[start]))}')
    logging.debug(f'    {lines[start+1]}-> set: {sorted(set(lines[start+1]))}')
    logging.debug(f'    {lines[start+2]}-> set: {sorted(set(lines[start+2]))}')

print(f'The sum of the badge priorities is {badge_sums}')
    