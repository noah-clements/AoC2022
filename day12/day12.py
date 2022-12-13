from aocd import data
import logging
import string
# import numpy as np
import math
from collections import deque

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

def parse(puzzle_input):
    """Parse input."""
    letter_vals = string.ascii_lowercase 
    return [[letter_vals.find(char) if char in letter_vals else char for char in line] for line in puzzle_input.splitlines()]

def get_location(maze:list[list], char):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == char:
                return (i, j)

def fix_wandering(path:list, topo):
    for i in range(len(path)):
        for j in range(len(path) - 1, i + 1, -1):
            if math.dist(path[i], path[j]) == 1:
                ih, iw = path[i]
                jh, jw = path[j]
                if (topo[jh][jw] - topo[ih][iw]) <= 1:
                    logging.debug(f'fixing path {path[i]} and {path[j]}')
                    # logging.debug(f'fixing path:{path[:i+1] + path[j:]}')
                    return path[:i+1] + path[j:]
    return path

def get_max_next_loc(location, grid, path:list, nogos:set):
    x, y = location
    current_val = grid[x][y]
    potential_next = location
    for nx, ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
        if (0 <= nx < len(grid) and 0 <= ny < len(grid[0]) 
            and (nx, ny) not in path
            and (nx, ny) not in nogos):
                if grid[nx][ny] - current_val == 1:
                    return (nx, ny)
                elif grid[nx][ny] == current_val:
                    potential_next = (nx, ny)
    return potential_next
    
    
def old_part1(topo):
    starting_loc = get_location(topo, 'S')
    destination = get_location(topo, 'E')
    # now replace the 'S' & 'E' characters with their values
    x,y = starting_loc
    topo[x][y] = 0
    x,y = destination
    topo[x][y] = 25
    current_loc = starting_loc
    path = []
    no_gos = set()
    while current_loc!= destination:
        next_loc = get_max_next_loc(current_loc, topo, path, no_gos)
        if next_loc == current_loc:  # have to backtrack
            # no_gos.add(current_loc)
            current_loc = path.pop() if len(path) > 0 else starting_loc
            logging.debug(f'Backtracking from {next_loc} to {current_loc}')
        else:
            path.append(current_loc)
            current_loc = next_loc
    more_fixes = True
    while more_fixes:
        logging.debug('Going to try to fix the wandering path')
        new_path = fix_wandering(path, topo)
        if new_path == path:
            more_fixes = False
        else:
            path = new_path
    logging.debug(path)
    return len(path)

def part2(topo):
    """Solve part 2."""

def part1(grid):
    starting_loc = get_location(grid, 'S')
    destination = get_location(grid, 'E')
    # now replace the 'S' & 'E' characters with their values
    x,y = starting_loc
    grid[x][y] = 0
    x,y = destination
    grid[x][y] = 25
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
    

def solve(data):
    """Solve the puzzle for the given input."""
    topography = parse(data)
    for line in topography:
        logging.debug(line)
    solution1 = part1(topography)
    solution2 = part2(topography)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))

        # direction = np.sign(np.subtract(destination, current_loc))
        # direction[0] != 0 this test is not productive


        # if (topo[ch + direction[0]][cw] <= topo[ch][cw]+1 
        #     and (ch + direction[0], cw) not in no_gos
        #     and (ch + direction[0], cw) != current_loc):
        #     path.append(current_loc)
        #     current_loc = (ch + direction[0], cw)
        # elif (topo[ch][cw + direction[1]] <= topo[ch][cw]+1
        #       and (ch, cw + direction[1]) not in no_gos
        #       and (ch, cw + direction[1])!= current_loc):
        #     path.append(current_loc)
        #     current_loc = (ch, cw + direction[1])            # path = fix_wandering(path, current_loc)

        # if (len(topo) > ch + 1
        #       and topo[ch + 1][cw] == current_val + 1 
        #       and (ch + 1, cw) not in no_gos
        #       and (ch + 1, cw) not in path):
        #     path.append(current_loc)
        #     current_loc = (ch + 1, cw)
        # elif (ch > 0 and topo[ch - 1][cw] == current_val + 1   
        #       and (ch - 1, cw) not in no_gos
        #       and (ch - 1, cw) not in path):
        #     path.append(current_loc)
        #     current_loc = (ch -1, cw)
        # elif (len(topo[ch]) > cw + 1
        #       and topo[ch][cw + 1] == current_val + 1  
        #       and (ch, cw + 1) not in no_gos
        #       and (ch, cw + 1) not in path):
        #     path.append(current_loc)
        #     current_loc = (ch, cw +1)
        # elif (cw > 0 and topo[ch][cw - 1] == current_val + 1 
        #       and (ch, cw - 1) not in no_gos
        #       and (ch, cw - 1) not in path):
        #     path.append(current_loc)
        #     current_loc = (ch, cw - 1)