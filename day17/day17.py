from aocd import data
import logging
from functools import wraps
from time import time

from rocks import RockFactory, Rock

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
def part1(data, num_rocks):
    """Solve part 1."""
    # cavern = {}
    rf = RockFactory()
    top_y = 0
    jet_length = len(data)
    jet_idx = 0
    for _ in range(num_rocks):
        rock = rf.get_next_rock(top_y)
        still_falling = True
        while still_falling:
            current_jet = data[jet_idx % jet_length]
            if current_jet == '<':
                rock.move_left()
            else:
                rock.move_right()
            jet_idx += 1
            still_falling, top_y = rock.fall()
    # logging.debug(rock._cavern)
    return top_y

@measure
def part2(parsed_data):
    """Solve part 2."""

def solve(data):
    """Solve the puzzle for the given input."""
    solution1 = part1(data, 2022)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))
    logging.debug(data)