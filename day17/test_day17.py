# test_aoc_template.py

import pathlib
import pytest
import logging
import day17 as aoc
from rocks import Rock

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    # puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    result = aoc.collapse(example1, 2022)
    # logging.debug(len(Rock._cavern))
    logging.debug(Rock._cavern)
    assert result == 3068

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.collapse(example1, 1_000_000_000_000) == 1514285714288

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...