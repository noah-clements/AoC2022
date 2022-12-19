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
def collapse(data, num_rocks, jet_idx=0):
    """Solve part 1."""
    # cavern = {}
    rf = RockFactory()
    top_y = 0
    jet_length = len(data)
    for i in range(num_rocks):
        # logging.debug(f"Rock number: {i}")
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
    return top_y, jet_idx

@measure
def pattern_collapse(data, num_rocks):
    # last_mult_top_y = collapse(data, 5)
    # possible_pattern = False
    top_y = 0
    jet_length = len(data)
    lcm = jet_length if jet_length % 5 ==0 else jet_length * 5
    jet_idx = 0
    if num_rocks > lcm:
        logging.debug(f'more than lcm pattern {lcm}')
        top_y, jet_idx = collapse(data, lcm, jet_idx)
        multiplier = num_rocks // lcm
        top_y = multiplier * top_y
        jet_idx *= multiplier + 1

    remainder = num_rocks % lcm
    next_y, _ = collapse(data, remainder, jet_idx)
    top_y += next_y
    
    return top_y



def solve(data):
    """Solve the puzzle for the given input."""
    solution1, _ = collapse(data, 200_000)
    logging.debug(f'instructions: {len(data)}. Last character: {data[-1]}')
    Rock.reset_cavern()
    solution2 = pattern_collapse(data, 200_000)
    # solution2 = None

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))
    # logging.debug(data)