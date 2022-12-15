from aocd import data
import logging
from functools import wraps
from time import time
import re

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
    ping_re = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): '
                         r'closest beacon is at x=(-?\d+), y=(-?\d+)')

    sensor_distances = {}
    beacons = {}
    for line in puzzle_input.splitlines():
        match = ping_re.match(line)
        if match:
            sx, sy = int(match.group(1)), int(match.group(2))
            bx, by = int(match.group(3)), int(match.group(4))
            sensor_distances[sx, sy] = abs(sx -bx) + abs(sy - by)
            try:
                beacons[bx, by].append((sx, sy))
            except KeyError:
                beacons[bx, by] = [(sx, sy)]
    logging.debug(sensor_distances)
    logging.debug(beacons)
    return sensor_distances, beacons

@measure
def part1(parsed_data):
    """Solve part 1."""

@measure
def part2(parsed_data):
    """Solve part 2."""

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