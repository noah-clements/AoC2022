from aocd import data
# import logging

# logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')
# # logging.disable(logging.CRITICAL)
# logging.info('Start of program')

def parse(puzzle_input):
    return [(line.split()[0], int(line.split()[1])) 
            if len(line.split()) > 1 else (line)
            for line in puzzle_input.splitlines()]

def part1(instructions:[]):
    regx = 1
    addx_cycle = 2 
    cycle = 0
    strength_sum = 0
    measurements = [(40 * i + 20) for i in range(6)]
    measurements.reverse()
    next_measurement = measurements.pop()
    for instruction in instructions:
        addx = 0
        if instruction[0] == 'addx':
            addx = instruction[1]
            cycle += addx_cycle
        else:
            cycle += 1

        if cycle >= next_measurement: # we're in the middle of adding, can't include.
            strength_sum += regx * next_measurement
            regx += addx
            if measurements:
                next_measurement = measurements.pop()
            else:
                break
        else:
            regx += addx
    return strength_sum        

def part2(instructions:[]):
    regx = 1
    addx_cycle = 2 
    cycle = 0
    crt_out = ''
    instructions.reverse()
    action = instructions.pop()
    for _ in range(6): # i is crt row
        for j in range(40):  # j is crt position
            # draw crt  before instruction
            #stole this from flowernal
            crt_out += '🌕' if regx - 1 <= j <= regx + 1 else '🌑'

            if action[0] == 'addx':  # take 2
                cycle += 1
                if cycle % addx_cycle == 0:
                    regx += action[1]
                    cycle = 0
                    if len(instructions) > 0:
                        action = instructions.pop()
                    else: 
                        break
            else:
                if len(instructions) > 0:
                    action = instructions.pop()
                else: 
                    break
        crt_out += '\n'
    return crt_out

def solve(data):
    """Solve the puzzle for the given input."""
    instructions = parse(data)
    solution1 = part1(instructions)
    solution2 = part2(instructions)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))