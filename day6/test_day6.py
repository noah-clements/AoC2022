# test_aoc_template.py

import pytest
import day6 as aoc

examples = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",11),
            ]

msg_examples = [('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
                ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
                ('nppdvjthqldpwncqszvftbrmjlhg', 23),
                ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',29),
                ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
                ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_examples():
    """Test part 1 on example input."""
    for example in examples:
        assert aoc.part1(example[0]) == example[1]

# @pytest.mark.skip(reason="Not implemented")
def test_part2_examples():
    """Test part 2 on example input."""
    for example in msg_examples:
        assert aoc.part2(example[0]) == example[1]

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...