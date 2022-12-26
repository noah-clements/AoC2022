from aocd import data
import logging
from functools import wraps, cache
from time import time
from operator import itemgetter
import sys

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


def find_water_sides(cubes):
    max_x = max(cubes, key=itemgetter(0))[0] + 2
    min_x = min(cubes, key=itemgetter(0))[0] - 1
    max_y = max(cubes, key=itemgetter(1))[1] + 2
    min_y = min(cubes, key=itemgetter(1))[1] - 1
    max_z = max(cubes, key=itemgetter(2))[2] + 2
    min_z = min(cubes, key=itemgetter(2))[2] - 1

    water = [(min_x, min_y, min_z)] # just as we'd start a recursive flood fill
    water_sides = 0
    visited = [] # dfs cache

    # do an iterative flood fill - python max recusion
    while water:
        x, y, z = water.pop()
        if (x, y, z) not in visited:
            visited.append((x, y, z))

            # stole this efficient loop of flood points from u/alykzandr
            for nx,ny,nz in [(x + 1, y, z), (x - 1, y, z),
                             (x, y + 1, z), (x, y - 1, z),
                             (x, y, z + 1), (x, y, z - 1)]:
                if (min_x <= nx <= max_x and 
                    min_y <= ny <= max_y and
                    min_z <= nz <= max_z):
                    if (nx,ny,nz) in cubes:
                        water_sides += 1
                    else:
                        water.append((nx,ny,nz))
    return water_sides

@measure
def part1(cubes):
    """Solve part 1."""
    return count_exposed_sides(cubes)    

@measure
def part2(blocks):
    # using global var so that 
    # the recursion memoization cache can be used
    return find_water_sides(blocks)

def solve(data):
    parsed_data = parse(data)
    solution1 = part1(parsed_data)
    # reload - as in pytest, this parsed data is a fixture
    # parsed_data = parse(data)
    solution2 = part2(parsed_data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))