from aocd import data
import logging
from functools import wraps, cache
from time import time
from operator import itemgetter
import itertools

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

max_x, min_x, max_y, min_y, max_z, min_z = 0,0,0,0,0,0
water = []


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

# @cache
def flood_fill(cubes, x, y, z):
    global water
    # return if at edges
    if (x < min_x or x == max_x or 
        y < min_y or y == max_y or 
        z < min_z or z == max_z):
        return
    # been here before or hit a cube
    if ((x,y,z) in water or (x,y,z) in cubes):
        return

    water.append((x,y,z))

    # spread out - the fill
    flood_fill(cubes, x + 1, y, z)
    flood_fill(cubes, x - 1, y, z)
    flood_fill(cubes, x, y + 1, z)
    flood_fill(cubes, x, y - 1, z)
    flood_fill(cubes, x, y, z + 1)
    flood_fill(cubes, x, y, z - 1)


def find_water_sides(cubes):
    global max_x, min_x, max_y, min_y, max_z, min_z
    global water
    max_x = max(cubes, key=itemgetter(0))[0] + 2
    min_x = min(0, min(cubes, key=itemgetter(0))[0] - 2)
    max_y = max(cubes, key=itemgetter(1))[1] + 2
    min_y = min(0, min(cubes, key=itemgetter(1))[1] - 2)
    max_z = max(cubes, key=itemgetter(2))[2] + 2
    min_z = min(0, min(cubes, key=itemgetter(2))[2] - 2)

    flood_fill(cubes, 0,0,0) # flood fill starts with 0,0,0
    water_sides = 0

    for cube in cubes:
        x, y, z = cube
        if ((x-1, y, z) not in cubes and
            len(set(itertools.product(range(min_x, x-1), [y], [z])) & set(cubes)) == 1):
            cubes_w_gaps.append(cube)
        elif ((x+1, y, z) not in cubes and
              len(set(itertools.product(range(x+2, max_x+1), [y], [z])) & set(cubes)) == 1):
            cubes_w_gaps.append(cube)
        elif ((x, y-1, z) not in cubes and
              len(set(itertools.product([x], range(min_y, y-1), [z])) & set(cubes)) == 1):
            cubes_w_gaps.append(cube)
        elif ((x, y+1, z) not in cubes and
              len(set(itertools.product([x], range(y+2, max_y+1), [z])) & set(cubes)) == 1):
            cubes_w_gaps.append(cube)
        elif ((x, y, z-1) not in cubes and
              len(set(itertools.product([x], [y], range(min_z, z-1))) & set(cubes)) == 1):
            #   (x,y,z-2) in cubes):
            cubes_w_gaps.append(cube)
        elif ((x, y, z+1) not in cubes and
              len(set(itertools.product([x], [y], range(z+2, max_z+1))) & set(cubes)) == 1):
            cubes_w_gaps.append(cube)
    logging.debug(cubes_w_gaps)
    return cubes_w_gaps

@measure
def part1(cubes):
    """Solve part 1."""
    return count_exposed_sides(cubes)    


@measure
def part2(cubes):
    """Solve part 2."""
    return count_exposed_sides(cubes) - len(find_water_sides(cubes))

def solve(data):
    """Solve the puzzle for the given input."""
    parsed_data = parse(data)
    solution1 = part1(parsed_data)
    # reload - as in pytest, this parsed data is a fixture
    # parsed_data = parse(data)
    solution2 = part_2(parsed_data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))