from aocd import data
import logging

logging.basicConfig(filename='day6.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')


def part1(data):
    """Solve part 1."""
    for i in range(4, len(data)):
        if len(set(data[i-4:i])) < 4:
            logging.debug(f'{data[i-4:i]} is NOT the marker.')
            continue
        else:
            logging.debug(f'{data[i-4:i]} IS the marker.')
            return i

def part2(data):
    """Solve part 2."""
    for i in range(14, len(data)):
        if len(set(data[i-14:i])) < 14:
            logging.debug(f'{data[i-14:i]} is NOT the message.')
            continue
        else:
            logging.debug(f'{data[i-14:i]} IS the message.')
            return i
    
print(f'The marker position is {part1(data)}')
print(f'The message position is {part2(data)}')
print([[i for i in range(j,len(data))if len(set(data[i-j:i]))==j][0]for j in[4,14]])
