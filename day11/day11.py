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
    '*' : operator.mul
    }

lcm = 1


class Monkey():
    def __init__(self, monkey_number:int, starting_items:list, operation:str, 
                 operand, divisor_test:int, true_monkey:int, false_monkey:int):
        self.number = monkey_number
        self.inspections = 0
        self.item_worries = [int(item) for item in starting_items]
        # operator suggested by ChatGPT, 
        # but it 'thought' I could use getattr()
        self.op = ops[operation]
        self.operation = operation
        try:
            self.operand = int(operand)
            self.old_op = False
        except:
            self.operand = operand
            self.old_op = True
        self.divisor = divisor_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

    def __repr__(self) -> str:
        return (f'Monkey({self.number}, {self.item_worries}, ' +
                f'{next(key for key, value in ops.items() if value == self.op)}, '+
                f'{self.operand}, {self.divisor}, ' +
                f'{self.true_monkey}, {self.false_monkey})')

    def inspect_and_throw(self, divide_worry=1):
        true_items = []
        false_items = []
        for item in self.item_worries:
            self.inspections += 1
            operand = item if self.old_op else self.operand
            item = self.op(item, operand)
            item %= lcm 
            if divide_worry > 1:
                item = item // divide_worry
            #inspect 
            if item % self.divisor == 0:  
                true_items.append(item)
            else:
                false_items.append(item)
        self.item_worries = []
        return [(self.true_monkey, true_items), (self.false_monkey, false_items)]

    def add_items(self, items):
        self.item_worries = self.item_worries + items 

    def get_inspections(self) -> int:
        return self.inspections


def parse(puzzle_input):
    """Parse input. Monkeys have list of starting items, 
    or registers, upon which operations are performed. 
    Then tests are performed on the register items and
    potential changes to the register items.
    Each 'Monkey' is separated from the others by \n\n
    """
    global lcm
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
                                  [item for item in (matches.group(2).split(','))],
                                  matches.group(5),
                                  matches.group(6),
                                  int(matches.group(7)),
                                  int(matches.group(8)),
                                  int(matches.group(9))))
            lcm *= int(matches.group(7))
    return monkeys


def watch_monkeys(monkeys:[Monkey], rounds:int, divide_worry:int=1):
    for i in range(rounds):
        for monkey in monkeys:
            reallocate = monkey.inspect_and_throw(divide_worry)
            for item in reallocate: 
                monkeys[item[0]].add_items(item[1])
        if (i +1) <= 100:
            logging.debug(f'Run {i +  1} {[monkey.get_inspections() for monkey in monkeys]}')
    inspections = [monkey.get_inspections() for monkey in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

def part2(monkeys:[Monkey]):
    """Solve part 2."""

def solve(data):
    """Solve the puzzle for the given input."""
    monkeys = parse(data)
    logging.debug("about to start part 1")
    solution1 = watch_monkeys(monkeys, rounds=20, divide_worry=3)
    logging.debug("about to start part 2")
    monkeys = parse(data)
    solution2 = watch_monkeys(monkeys, rounds=10_000)
    logging.debug("ended part 2")

    return solution1, solution2

if __name__ == "__main__":
    # with open('input.txt') as f:
    #     data = f.read().strip()
    solutions = solve(data)
    print("\n".join(str(solution) for solution in solutions))