from aocd import data
import logging
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

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

@measure
def parse(puzzle_input):
    """Parse input."""
    blocks =  [tuple(int(x) for x in line.strip().split(',')) for line in puzzle_input.splitlines()]
    return blocks


# ChatGPT ended up refactoring its first attempt.
# Unlike the original, I didn't have to correct the code 
# and this one was more simple and efficient. I got it by asking 
# about exterior exposed sides, and it ended up give me correct all (not exterior) sides.
def find_exposed_sides(cubes):
    exposed_sides = {}
    for cube in cubes:
        exposed_sides[cube] = []
        x, y, z = cube
        if (x-1, y, z) not in cubes:
            exposed_sides[cube].append("left")
        if (x+1, y, z) not in cubes:
            exposed_sides[cube].append("right")
        if (x, y-1, z) not in cubes:
            exposed_sides[cube].append("top")
        if (x, y+1, z) not in cubes:
            exposed_sides[cube].append("bottom")
        if (x, y, z-1) not in cubes:
            exposed_sides[cube].append("front")
        if (x, y, z+1) not in cubes:
            exposed_sides[cube].append("back")
    return exposed_sides

def count_exposed_sides(cubes):
    exposed_sides = find_exposed_sides(cubes)
    logging.debug(exposed_sides)
    count = 0
    for cube, sides in exposed_sides.items():
        count += len(sides)
    return count



@measure
def part1(cubes):
    """Solve part 1."""
    return count_exposed_sides(cubes)    


@measure
def part2(cubes):
    """Solve part 2."""
    return count_exposed_sides(cubes)

def solve(data):
    """Solve the puzzle for the given input."""
    parsed_data = parse(data)
    solution1 = part1(parsed_data)
    # reload - as in pytest, this parsed data is a fixture
    # parsed_data = parse(data)
    solution2 = part2(parsed_data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))