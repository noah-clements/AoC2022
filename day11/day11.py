from aocd import data
import logging
import operator
import re 

logging.basicConfig(filename='aoc.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

class Monkey():
    def __init__(self, monkey_number:int, starting_items:list, operation:str, 
                 operand, devisor_test:int, true_monkey:int, false_monkey:int):
        self.number = monkey_number
        self.items = starting_items
        self.uncommitted_items = []
        # operator suggested by ChatGPT, 
        # but it 'thought' I could use getattr()
        self.op = ops[operation]
        try:
            self.operand = int(operand)
        except:
            self.operand = operand
            self.old_op = True
        self.devisor = devisor_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def __repr__(self) -> str:
        return (f'Monkey({self.number}, {self.items}, ' +
                f'{next(key for key, value in ops.items() if value == self.op)}, '+
                f'{self.operand}, {self.devisor}, ' +
                f'{self.true_monkey}, {self.false_monkey})')

    def operate(self):
        for item in self.items:
            operand = item if self.old_op else self.operand
            item = self.op(item, operand)

    def add_items(self, items:list):
        self.uncommitted_items = items

    def commit(self):
        self.items = self.uncommitted_items
        self.uncommitted_items = []

    def reallocate(self):
        true_items = []
        false_items = []
        for item in self.items:
            if item % self.devisor == 0:
                true_items.append(item)
            else:
                false_items.append(item)
        self.items = []
        return {self.true_monkey: true_items, self.false_monkey: false_items}


def parse(puzzle_input):
    """Parse input. Monkeys have list of starting items, 
    or registers, upon which operations are performed. 
    Then tests are performed on the register items and
    potential changes to the register items.
    Each 'Monkey' is separated from the others by \n\n
    """
    prog = re.compile(r'Monkey (\d+):\s+Starting items: ((\d+(, )?)+)\s+'
                        r'Operation: new = old ([+-/*]) (\d+|old)\s+'
                        r'Test: divisible by (\d+)\s+'
                        r'If true: throw to monkey (\d+)\s+'
                        r'If false: throw to monkey (\d+)')
    monkey_sects =  puzzle_input.split('\n\n')
    monkeys = []
    for sect in monkey_sects:
        matches = prog.match(sect)
        if matches:
            monkeys.append(Monkey(int(matches.group(1)),
                                  [int(item) for item in (matches.group(2).split(','))],
                                  matches.group(5),
                                  matches.group(6),
                                  int(matches.group(7)),
                                  int(matches.group(8)),
                                  int(matches.group(9))))
    return monkeys


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