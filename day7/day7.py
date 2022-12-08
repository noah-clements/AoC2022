# aoc_template.py

from aocd import data
import logging
import re 

logging.basicConfig(filename='day7.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

MIN_SPACE = 30000000
DISK_SIZE = 70000000

def add_sub_directory():
    return {
        'dir': {},
        'file': {},
        'size': 0
    }

def parse(puzzle_input):
    dir_re = re.compile(r'\$ cd (.*)')
    file_re = re.compile(r'(\d+) (.*)')
    add_dir_re = re.compile(r'dir (.*)')
    ls_re = re.compile(r'\$ ls')
    file_sys = {'/':None,}
    file_sys['/'] = add_sub_directory()
    current_dir = file_sys['/']
    parent_dir = [file_sys['/'],]
       
    lines = puzzle_input.splitlines()
    for line in lines:
        match = dir_re.match(line)
        if match:
            dir = match.group(1)
            if dir == '..':
                current_dir = parent_dir.pop()
            elif dir == '/':
                current_dir=file_sys[dir]
            continue
        match = file_re.match(line)
        if match:
            file_name = match.group(2)
            file_size = int(match.group(1))
            current_dir['file'][file_name] = file_size
            for parent in parent_dir:
                parent['size'] += file_size
            continue
        match = add_dir_re.match(line)
        if match:
            current_dir['dir'][match.group(1)] = None
            continue
        match = ls_re.match(line)
        if match and dir != '/':
            current_dir = add_sub_directory()
            parent_dir[-1]['dir'][dir] = current_dir
            parent_dir.append(current_dir)
            continue
    return file_sys            
        
def sum_subdir_sizes(starting_dir:dict, search_size:int):
    sub_dir_sum = 0    
    for sub_dir in starting_dir['dir'].values():
        if len(sub_dir) > 0:
            sub_dir_sum += sum_subdir_sizes(sub_dir, search_size)
        if sub_dir['size'] <= search_size:
            logging.debug(f'Sum={sub_dir_sum}, adding {sub_dir["size"]}')
            sub_dir_sum += sub_dir['size']
    return sub_dir_sum            

def part1(file_sys: dict):
    search_size = 100000
    starting_dir = file_sys['/']
    return sum_subdir_sizes(starting_dir, search_size)

def get_smallest_needed_subdir(starting_dir:dict, current_smallest:int, needed_space:int):
    smallest_size = current_smallest
    for sub_dir in starting_dir['dir'].values():
        if len(sub_dir) > 0:
            smallest_size = get_smallest_needed_subdir(sub_dir, smallest_size, needed_space)
        if needed_space <= sub_dir['size'] < smallest_size:
            logging.debug(f'current_smallest={smallest_size}, replacing with {sub_dir["size"]}')
            smallest_size = sub_dir['size']
    return smallest_size

def part2(file_sys: dict):
    free_space = DISK_SIZE - file_sys['/']['size']
    needed_space = MIN_SPACE - free_space
    logging.debug(f'needed_space={needed_space}')
    starting_dir = file_sys['/']
    return get_smallest_needed_subdir(starting_dir, starting_dir['size'], needed_space)
    
file_sys = parse(data)
print(f'part1: {part1(file_sys)}')
print(f'part2: {part2(file_sys)}')

