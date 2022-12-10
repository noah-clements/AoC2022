from aocd import data
import math
import numpy as np

direction = {
    'U': (0,1),
    'D': (0,-1),
    'L': (-1,0),
    'R': (1,0),
}

def parse(puzzle_input):
    # convert to list of tuples we can loop through -> [(dir, times)]
    instructions =  [(line.split()[0], int(line.split()[1])) for line in puzzle_input.splitlines()]
    return instructions

def move(instructions:list, second:bool):
    h_loc = (0,0) # starting head location
    body_loc = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),] 
    t_loc = (0,0) # tail location
    tail_positions = {t_loc}
    for instruction in instructions:
        times = instruction[1]
        movement = np.array(direction[instruction[0]])
        for _ in range(times):
            h_loc = (h_loc[0]+movement[0], h_loc[1]+movement[1])
            prev_section = h_loc
            if second:
                for i in range(len(body_loc)):
                    if math.dist(prev_section, body_loc[i]) >= 2:
                        distances = np.subtract(prev_section, body_loc[i])
                        body_loc[i] = tuple(np.add(body_loc[i], np.sign(distances)))
                    prev_section = body_loc[i]
            if math.dist(prev_section, t_loc) >= 2:
                distances = np.subtract(prev_section, t_loc)
                t_loc = tuple(np.add(t_loc, np.sign(distances)))
                tail_positions.add(t_loc)
    return len(tail_positions)

def solve(data):
    """Solve the puzzle for the given input."""
    instructions = parse(data)
    solution1 = move(instructions, second=False)
    solution2 = move(instructions, second=True)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))