from aocd import data
import logging
import ast
import numpy as np

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

def build_list(level:ast.List):
    result_list = []
    for item in level.elts:
        if isinstance(item, ast.List):
            result_list.append(build_list(item))
        elif isinstance(item, ast.Constant):
            result_list.append(item.value)
    logging.debug(f"in build_list: {result_list}")
    return result_list

def parse(puzzle_input):
    """Parse input."""
    return [[build_list(ast.parse(line, mode='eval').body) 
             for line in pair.splitlines()] 
            for pair in puzzle_input.split('\n\n')]

def in_order(left, right): 
    for i in range(len(left)):
        if i > len(right) - 1:
            return False
        elif type(left[i]) == int:
            if type(right[i]) == int:
                if left[i] > right[i]:
                    return False
                elif left[i] < right[i]:
                    return True
                else:
                    continue
            else:
                #convert int to list if necessary
                if not in_order([left[i]], right[i]):
                    return False
        elif type(left[i]) == list:
            #convert int to list if necessary
            right_val = ([right[i]] if type(right[i]) == int
                         else right[i])
            if not in_order(left[i], right_val):
                return False
    # even if the left & right were same length, 
    # would still be in correct order.
    return True

def part1(parsed_data):
    """Solve part 1."""
    sum_of_indices = 0
    for i in range(len(parsed_data)):
        left, right = parsed_data[i] 
        if in_order(left, right):
            sum_of_indices += i + 1
    return sum_of_indices
        

def part2(parsed_data):
    """Solve part 2."""

def solve(data):
    """Solve the puzzle for the given input."""
    parsed_data = parse(data)
    solution1 = part1(parsed_data)
    # reload - as in pytest, this parsed data is a fixture
    parsed_data = parse(data)
    solution2 = part2(parsed_data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))