from aocd import data
import logging
import ast
import json

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
    # for pair in pairs:
    #     for individual in pair:
    #         print(type(individual))
    #         logging.debug(f'individual: {ast.dump(individual, indent=2)}')
    #         logging.debug(f'value:{build_list(individual.body)}')
    #         # logging.debug(f'compiled individual: {compile(individual, "<string>", mode="single").eval()}')
    # puzzle = ast.parse(puzzle_input)
    # logging.debug(ast.dump(puzzle, indent=2))
    # print(ast.dump(puzzle, indent=2))
    # return pairs


def part1(parsed_data):
    """Solve part 1."""

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