from aocd import data
import logging
import numpy as np
import operator

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.info('Start of program')

from functools import wraps
from time import time
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it

@measure
def parse(puzzle_input):
    path_points = [[tuple(int(item) for item in point.strip().split(',')) for point in line.split('->')] for line in puzzle_input.splitlines()]
    logging.debug(path_points)
    rocks = {}
    for path in path_points:
        rocks[path[0]] = 'r'
        for i in range(1, len(path)):
            rocks[path[i]] = 'r'
            vector = np.subtract(path[i], path[i-1])
            direction = np.sign(vector)
            current_rock = path[i-1]
            while current_rock != path[i]:
                rocks[current_rock] = 'r'
                current_rock = tuple(np.add(current_rock, direction))
    logging.debug(rocks)
    logging.debug(f'max y = {max(rocks.keys(), key=operator.itemgetter(1))}')
    logging.debug(f'min y = {min(rocks.keys(), key=operator.itemgetter(1))}')
    logging.debug(f'max x = {max(rocks.keys())}; min x = {min(rocks.keys())}')
    return rocks

@measure
def fill_sand(cavern:dict, part2=False):
    more_sand = True
    max_y = max(cavern.keys(), key=operator.itemgetter(1))[1]
    if part2:
        max_y += 2
    print(f'part? {1 if not part2 else 2} max_y: {max_y}')
    start_pos =  (500,0)
    while more_sand:
        sand_pos = start_pos  # always start here
        at_rest = False
        while not at_rest:
            x, y = sand_pos
            test_pos = (x, y+1)
            if test_pos in cavern:
                test_pos = (x-1, y+1)
                if test_pos in cavern:
                    test_pos = (x+1, y+1)
                    if test_pos in cavern:
                        cavern[sand_pos] = 's'
                        at_rest = True
                        if sand_pos == start_pos:
                            more_sand = False
            sand_pos = test_pos
            if part2: 
                if sand_pos[1] == max_y - 1:
                    cavern[sand_pos] = 's'
                    at_rest = True
            elif sand_pos[1] > max_y:
                at_rest = True
                more_sand = False
    logging.debug(f'Ending sand positions: {sorted([key for key in cavern.keys() if cavern[key] == "s"])}')
    return len([key for key in cavern.keys() if cavern[key] == "s"])

def solve(data):
    """Solve the puzzle for the given input."""
    parsed_data = parse(data)
    solution1 = fill_sand(parsed_data)
    # Turns out that I don't need to reset the data, as pt 2 just adds on
    # parsed_data = parse(data)
    solution2 = fill_sand(parsed_data, part2=True)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))