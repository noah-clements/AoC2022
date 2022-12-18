# test_aoc_template.py

import pathlib
import pytest
import day16 as aoc
import logging
from day16 import Valve

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
logging.info('Start of program')

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented"
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    logging.debug(example1)
    store_dict, _ = example1
    comparator = {
        'AA':Valve('AA', 0, {'DD', 'II', 'BB'}),
        'BB':Valve('BB', 13, {'CC', 'AA'}),
        'CC':Valve('CC', 2, {'DD', 'BB'}),
        'DD':Valve('DD', 20, {'CC', 'AA', 'EE'}),
        'EE':Valve('EE', 3, {'FF', 'DD'}),
        'FF':Valve('FF', 0, {'EE', 'GG'}),
        'GG':Valve('GG', 0, {'FF', 'HH'}),
        'HH':Valve('HH', 22, {'GG'}),
        'II':Valve('II', 0, {'AA', 'JJ'}),
        'JJ':Valve('JJ', 21, {'II'}),
    }
    logging.debug(comparator)
    assert store_dict == comparator

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 1651

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 1707

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...