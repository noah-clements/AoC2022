# test_aoc_template.py

import pathlib
import pytest
import day15 as aoc

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
    sensors, beacons = example1
    assert sensors == {(2,18): 7, (9,16):1, (13,2):3, (12,14):4, 
                       (10,20):4, (14,17):5, (8,7):9, (2,0):10,
                       (0,11):3, (20,14):8, (17,20):6, (16,7):5,
                       (14,3):1, (20,1):7,
                       }
    assert beacons == {(-2,15):[(2,18)], 
                       (10,16):[(9,16), (12,14), (10,20), (14,17)],
                       (15,3):[(13,2), (16,7), (14,3), (20,1)],
                       (2,10):[(8,7), (2,0), (0,11)],
                       (25,17):[(20,14)],
                       (21,22):[(17,20)],
                       } 

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...