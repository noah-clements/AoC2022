# test_aoc_template.py

import pathlib
import pytest
import day7 as aoc

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
    root_dir = {'/':
        {'dir': {},
         'file': {'b.txt': 14848514,
                  'c.dat': 8504156,},
          'size':48381165}}

    
    a_dir = {
        'dir': {},
        'file': {'f':29116,
                 'g':2557,
                 'h.lst':62596
                 },
        'size': 94853
        }
    e_dir = {
        'dir': {},
        'file': {'i': 584},
        'size': 584
        }
    a_dir['dir']['e'] = e_dir

    d_dir = {
        'dir': {},
        'file': {'j':4060174,
                 'd.log':8033020,
                 'd.ext':5626152,
                 'k':7214296,
                 },
        'size': 24933642
        }
    
    root_dir['/']['dir']['a'] = a_dir
    root_dir['/']['dir']['d'] = d_dir

    
    assert example1 == root_dir

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