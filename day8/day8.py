from aocd import data
import logging

logging.basicConfig(filename='day8.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

def parse(puzzle_input):
    """Parse input."""

def part1(parsed_data):
    """Solve part 1."""

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