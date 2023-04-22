from aocd import data
import logging
from functools import wraps
from time import time
from itertools import cycle
from collections import defaultdict

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


# @measure
def collapse(data, num_rocks, current_y=0, jet_idx=0):
    """Solve part 1."""
    # cavern = {}
    rf = RockFactory()
    jet_length = len(data)
    for i in range(num_rocks):
        # logging.debug(f"Rock number: {i}")
        rock = rf.get_next_rock(current_y)
        still_falling = True
        while still_falling:
            current_jet = data[jet_idx % jet_length]
            if current_jet == '<':
                rock.move_left()
            else:
                rock.move_right()
            jet_idx += 1
            still_falling, current_y = rock.fall()
    # logging.debug(rock._cavern)
    return current_y, jet_idx % jet_length

# Use the logic from the bitmap state machine 
@measure
def pattern_collapse(jets, num_rocks):
    jet_factory = cycle(enumerate(jets))
    # Can use cycle(enumerate(rock|jet)) as factory pattern
    top_y = 0
    heights = []
    tracked = defaultdict(list)  # (rock_idx, jet_idx) -> top_y
    cycle_length = 0
    cycle_height = 0
    pre_cycle = 0
    levels = []
    rf = RockFactory()
    while not cycle_length:
        # logging.debug(f"Rock number: {i}")
        rock = rf.get_next_rock(top_y)
        still_falling = True
        while still_falling:
            jet_idx, current_jet = next(jet_factory)
            if current_jet == '<':
                rock.move_left()
            else:
                rock.move_right()
            still_falling, top_y = rock.fall()
        heights.append(top_y)

        key = (rock.get_rock_index(), jet_idx)
        levels.append(Rock.get_top_level())
        tracked[key].append(top_y)
        # Find cycle - DOES NOT WORK
        for i, m in enumerate(tracked[key][:-1]):  # slice does not include the last element
            for b in tracked[key][:i]:
                if m - b == len(heights) - m and levels[b:m] == levels[m:]:
                    pre_cycle = m
                    cycle_length = m - b
                    cycle_height = top_y - heights[m-1] 

    height = cycle_height * ((num_rocks - pre_cycle) // cycle_length) + heights[pre_cycle + ((num_rocks - pre_cycle) % cycle_length)-1]
    return height

# This is stolen in full from u/aledesole
# just changed variable names so I could understand them
@measure
def part2(jets, num_rocks):
    jet_factory = cycle(enumerate(jets))
    # Can use cycle(enumerate(rock|jet)) as factory pattern
    rocks = cycle(enumerate([    
        [120],                  # 1111000
    # Cross rock
        [32,                    # 0100000
         112,                   # 1110000
         32],                   # 0100000
    # Reverse L - upside down b/c first element becomes lowest y
        [112,                   # 1110000
         16,                    # 0010000
         16],                   # 0010000
    # vert line
        [64, 64, 64, 64],       # 1000000
                                # 1000000
                                # 1000000
                                # 1000000
                                
        [96, 96]                # 1100000
                                # 1100000
    ]))

    cavern = []  # map
    rocks_at_rest = []  # sequence of positions of rocks at rest
    state_cache = defaultdict(list)  # (rock_idx, instruction_idx) -> rest_idx
    heights = []  # sequence of max heights
    L = cycle_length = cycle_height = 0  # prefix, cycle length and height per cycle

    # you can define function inside another in Python
    # bit math to determine fit
    def fits(rock, x, y):
        return not any(
            cavern[j] & rock[j - y] >> x 
            for j in range(y, min(len(cavern), y + len(rock)))
        ) and all(r >> x << x == r for r in rock)  # line remains intact means no wall

    while not cycle_length:
        ri, rock = next(rocks)
        x, y = 2, len(cavern) + 4  # starting position
        # play rock
        while y and fits(rock, x, y - 1):
            y -= 1
            ai, arrow = next(jet_factory)
            nx = max(0, x - 1) if arrow == "<" else min(7, x + 1) # x bound by walls
            x = nx if fits(rock, nx, y) else x

        # update map
        for j, r in enumerate(rock, start=y):
            if j < len(cavern):
                cavern[j] |= r >> x
            else:
                cavern.append(r >> x)
        heights.append(len(cavern))
        rocks_at_rest.append(x)

        # find cycle
        state_cache[(ri, ai)].append(len(rocks_at_rest))
        for i, m in enumerate(state_cache[(ri, ai)][:-1]):  # slice does not include the last element
            for b in state_cache[(ri, ai)][:i]:
                if m - b == len(rocks_at_rest) - m and rocks_at_rest[b:m] == rocks_at_rest[m:]:
                    L = m
                    cycle_length = m - b
                    cycle_height = len(cavern) - heights[m-1] 

    height = cycle_height * ((num_rocks - L) // cycle_length) + heights[L+((num_rocks - L) % cycle_length)-1]
    return height


def solve(data):
    """Solve the puzzle for the given input."""
    solution1, _ = collapse(data, 2022)
    logging.debug(f'instructions: {len(data)}. Last character: {data[-1]}')
    Rock.reset_cavern()
    solution2 = part2(data, 1_000_000_000_000)
    # solution2 = None
    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))
    # logging.debug(data)
    # Rock.reset_cavern()
    # print(f'Pattern collapse {pattern_collapse(data, 1_000_000_000_000)}')
