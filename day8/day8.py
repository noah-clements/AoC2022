from aocd import data
import logging
import numpy as np
from io import StringIO


logging.basicConfig(filename='day8.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

def parse(puzzle_input):
    """Parse input."""
    parsed_input = np.genfromtxt(StringIO(puzzle_input), 
                                 delimiter=1, autostrip=True,
                                 dtype=int)
    logging.debug(parsed_input)
    return parsed_input
    
def part1(parsed_data):
    # logging.debug()
    logging.debug(parsed_data.shape)
    len_x, len_y = parsed_data.shape
    # the -2 is to not double count the corners
    visible_trees = (len_x + len_y - 2) * 2  # edges
    for i in range(1, len_x - 1):
        for j in range(1, len_y - 1):
            tree = parsed_data[i, j]
            row = parsed_data[i,:]
            col = parsed_data[:,j]
            logging.debug(f'tree at {(i, j)} is {tree}')
            logging.debug(f'Row maxes are :{np.amax(row[0:j])} & {np.amax(row[j+1:len_x])}')
            logging.debug(f'Col maxes are :{np.amax(col[0:i])} & {np.amax(col[i+1:len_y])}')
                          
            if (tree > np.amax(row[0:j]) or
                tree > np.amax(row[j+1:len_x]) or
                tree > np.amax(col[0:i]) or
                tree > np.amax(col[i+1:len_y])):
                logging.debug(f'Tree is visible')
                visible_trees += 1
    return visible_trees   
    

def part2(parsed_data):
    """Solve part 2."""

def solve(data):
    """Solve the puzzle for the given input."""
    parsed_data = parse(data)
    solution1 = part1(parsed_data)
    solution2 = part2(parsed_data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))