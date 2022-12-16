from aocd import data
import logging
from functools import wraps
from time import time
import re
from sympy import RegularPolygon, Point

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
            beacons[sx, sy] = bx, by
            # try:
            #     beacons[bx, by].append((sx, sy))
            # except KeyError:
            #     beacons[bx, by] = [(sx, sy)]
    logging.debug(sensor_distances)
    # logging.debug(beacons)
    return sensor_distances, beacons

@measure
def part1(parsed_data, row):
    """Solve part 1."""
    not_there=set()
    beacon_x = set()
    sensor_distance, beacons = parsed_data
    for point, val in sensor_distance.items():
        sx, sy = point
        bx, by = beacons[sx, sy]
        if by == row:
            beacon_x.add(bx)
        if (window := val - abs(row- sy)) >= 0:
            not_there.update([x for x in range(sx-window, sx+window+1)])
    not_there.difference_update(beacon_x)
    return len(not_there)

@measure
def part2(parsed_data, max_value):
    x_mult = 4_000_000
    sensor_distance, _ = parsed_data
    checked_points = set()
    for point, val in sensor_distance.items():
        # boundaries.append(RegularPolygon(Point(point), val, 4))
        sx, sy = point
        for side in range(4):
            for i in range(val+1):
                if side == 0:
                    cx = sx + val + 1 - i
                    cy = sy + i
                elif side == 1:
                    cx = sx - i
                    cy = sy + val + 1 - i
                elif side == 2:
                    cx = sx - val - 1 + i
                    cy = sy - i
                else:               # side == 3
                    cx = sx + i
                    cy = sy - val - 1 + i
                if (0 <= cx <= max_value and 0 <= cy <= max_value
                    and (cx, cy) not in checked_points):
                    found = all((abs(cx - otherx) + abs(cy - othery)) > other_distance 
                                for (otherx, othery), other_distance in sensor_distance.items())
                if found:
                    return x_mult * cx + cy
                else:
                    checked_points.add((cx, cy))
                    
    logging.debug(f'Checked locations: {checked_points}')
            

def solve(data):
    """Solve the puzzle for the given input."""
    parsed_data = parse(data)
    solution1 = part1(parsed_data, 2_000_000)
    # reload - as in pytest, this parsed data is a fixture
    # parsed_data = parse(data)
    solution2 = part2(parsed_data, 4_000_000)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))