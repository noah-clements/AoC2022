# test_aoc_template.py

import pathlib
import pytest
import day14 as aoc

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
    """Test that input is parsed properly."""
    assert example1 == {
        (498,4):'r', (498,5):'r', (498,6):'r', (497,6):'r', (496,6):'r',
        (503,4):'r', (502,4):'r', (502,5):'r', (502,6):'r', (502,7):'r',
        (502,8):'r', (502,9):'r', (501,9):'r', (500,9):'r', (499,9):'r',
        (498,9):'r', (497,9):'r', (496,9):'r', (495,9):'r', (494,9):'r',
    }

# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.fill_sand(example1) == 24

# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.fill_sand(example1, part2=True) == 93

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...