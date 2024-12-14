"""Day 11 of Advent of Code 2024.

The goal of parts 1 and 2 are to find the number of stones created after
a certain number of blinks. The stones are either turned from 0 to 1, split
in half if they have an even number of digits, or multiplied by 2024 otherwise.
We can use a recursive function to find the number of stones after a certain
number of blinks.

Because of the recursive nature of the function, we can use a lru_cache to
cache the results of the function calls and improve the performance of the
function. Otherwise the function would be too slow or run out of memory.
"""

from day_starter import DayStarter
from functools import lru_cache


class AdventDay11:

    def __init__(self):
        self.data = [x.replace('\n', '') for x in DayStarter(11).split(' ')]
        self.part1 = self.blink_dfs(25, 'part1')
        self.part2 = self.blink_dfs(75, 'part2')

    def blink_dfs(self, blinks, part):
        """Uses a recursive function to find the number of stones after a
        certain number of blinks."""

        @lru_cache(maxsize=None)
        def dfs_helper(val: str, to_go):
            """Recursive function to find the number of stones after a certain
            number of blinks. The function will either turn a stone from 0 to
            1, split a stone in half if it has an even number of digits, or
            multiply a stone by 2024. The function will then call itself
            recursively for the new stone(s) created until the number of
            blinks is reached.
            """
            if to_go == 0:
                return 1
            if val == '0':
                return dfs_helper('1', to_go - 1)
            if len(val) % 2 == 0:
                n = len(val)//2
                left = val[:n]
                right = val[n:]
                while right.startswith('0') and len(right) > 1:
                    right = right[1:]
                return dfs_helper(left, to_go - 1) +\
                    dfs_helper(right, to_go - 1)
            else:
                return dfs_helper(str(int(val)*2024), to_go - 1)

        if part == 'part1':
            return sum([dfs_helper(val, blinks) for val in self.data])
        else:
            return sum([dfs_helper(val, blinks) for val in self.data])


if __name__ == '__main__':
    day11 = AdventDay11()
    print(day11.part1, day11.part2)
