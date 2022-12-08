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
    return parsed_input
    
def part1(tree_array):
    len_x, len_y = tree_array.shape
    # the -2 is to not double count the corners
    visible_trees = (len_x + len_y - 2) * 2  # edges
    for i in range(1, len_x - 1):
        for j in range(1, len_y - 1):
            tree = tree_array[i, j]
            row = tree_array[i,:]
            col = tree_array[:,j]                          
            if (tree > np.amax(row[0:j]) or
                tree > np.amax(row[j+1:len_x]) or
                tree > np.amax(col[0:i]) or
                tree > np.amax(col[i+1:len_y])):
                logging.debug(f'Tree is visible')
                visible_trees += 1
    return visible_trees

def get_visible_trees(tree_array, tree:int):
    visible_trees = 1
    for i in range(len(tree_array)):
        if tree > tree_array[i] and i < len(tree_array) - 1:
            visible_trees += 1
        else:
            break
    return visible_trees

def part2(tree_array):
    len_x, len_y = tree_array.shape
    # the -2 is to not double count the corners
    max_scenic_score = 0
    for i in range(1, len_x - 1):
        for j in range(1, len_y - 1):
            tree = tree_array[i, j]
            row = tree_array[i,:]
            col = tree_array[:,j]
            n = get_visible_trees(col[i-1::-1], tree)
            s = get_visible_trees(col[i+1:], tree)
            e = get_visible_trees(row[j-1::-1], tree)
            w = get_visible_trees(row[j+1:], tree)
            if (tree_score := n * s * e * w) > max_scenic_score:
                max_scenic_score = tree_score
    return max_scenic_score

def solve(data):
    """Solve the puzzle for the given input."""
    tree_array = parse(data)
    solution1 = part1(tree_array)
    solution2 = part2(tree_array)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))