# test_aoc_template.py

import pathlib
import pytest
import day11 as aoc
from day11 import Monkey

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    monkeys =[Monkey(0, [79, 98], '*', '19', 23, 2, 3),
              Monkey(1, [54,65,75,74], '+', '6', 19, 2, 0),
              Monkey(2, [79, 60, 97], '*', 'old', 13, 1, 3),
              Monkey(3, [74], '+', '3', 17, 0, 1),]
    assert repr(example1) == repr(monkeys)

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.watch_monkeys(example1, rounds=20, divide_worry=3) == 10605

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.watch_monkeys(example1, rounds=10000) == 2713310158

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...