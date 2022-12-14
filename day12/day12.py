from aocd import data
import logging
import string
from collections import deque

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.info('Start of program')

def parse(puzzle_input):
    """Parse input."""
    letter_vals = string.ascii_lowercase 
    return [[letter_vals.find(char) if char in letter_vals else char for char in line] for line in puzzle_input.splitlines()]

def get_locations(maze:list[list], char):
    locations = []
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == char:
                locations.append((i, j))
    return locations

def bfs_shortest_distance(grid, starting_loc, destination):
    queue = deque(((starting_loc, 0),))
    shortest_visited = {}
    shortest_path_length = float('inf')
    while queue:
        current_loc, steps = queue.popleft()
        next_steps = steps + 1
        x, y = current_loc
        shortest_visited[(x, y)] = steps
        if (x,y) == destination:
            shortest_path_length = min(shortest_path_length, steps)
        for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0])
                and grid[nx][ny] <= grid[x][y] + 1):
                # Check if neighbor is at most one unit higher than current_loc
                if ((nx, ny) not in shortest_visited 
                    or shortest_visited[(nx, ny)] > next_steps):
                    shortest_visited[(nx, ny)] = next_steps
                    # also add the neighbor to the queue
                    queue.append(((nx, ny), next_steps))
    return shortest_path_length


def part2(grid):
    starting_loc = get_locations(grid, 'S')[0]
    destination = get_locations(grid, 'E')[0]
    # now replace the 'S' & 'E' characters with their values
    x,y = starting_loc
    grid[x][y] = 0
    x,y = destination
    grid[x][y] = 25
    shortest_path_length = float('inf')
    possible_starts = get_locations(grid, 0)
    for start in possible_starts:
        shortest_path_length = min(shortest_path_length, bfs_shortest_distance(grid, start, destination))
    return shortest_path_length


def part1(grid):
    starting_loc = get_locations(grid, 'S')[0]
    destination = get_locations(grid, 'E')[0]
    # now replace the 'S' & 'E' characters with their values
    x,y = starting_loc
    grid[x][y] = 0
    x,y = destination
    grid[x][y] = 25
    return bfs_shortest_distance(grid, starting_loc, destination)
    

def solve(data):
    """Solve the puzzle for the given input."""
    topography = parse(data)
    for line in topography:
        logging.debug(line)
    solution1 = part1(topography)
    topography = parse(data)
    solution2 = part2(topography)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))
