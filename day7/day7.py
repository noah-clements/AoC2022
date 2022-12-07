# aoc_template.py

from aocd import data
import logging
import re 

logging.basicConfig(filename='day7.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')


def add_sub_directory():
    return {
        'dir': {},
        'file': {},
        'size': 0
    }


def parse(puzzle_input):
    """Parse input.
    Args:
        puzzle_input (str): Puzzle input.
    
    Returns:
        dict: file_sys.
        
    """
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
                # current_dir['size'] = sum([size for size in 
                #                            [val['size'] for val in current_dir['dir'].values()]]) 
                # current_dir['size'] += sum([size for size in current_dir['file'].values()])
                current_dir = parent_dir.pop()
            elif dir == '/':
                current_dir=file_sys[dir]
            # else:
            #     current_dir = current_dir['dir'][dir]
            #     parent_dir.append(current_dir)
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
            
        
        
        
        

def part1(data):
    """Solve part 1."""

def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

