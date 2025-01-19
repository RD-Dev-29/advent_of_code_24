""" Day 18 of Advent of Code 2024.

The goal is to find all possible ways to arrange towels in a desired pattern.
The towels are represented by strings of characters. The desired pattern is
represented by a string of characters. The goal of part 1 is to determine which
desired patterns can be achieved. The goal of part 2 is to determine how many
ways the desired patterns can be achieved.
"""

from day_starter import DayStarter
from functools import lru_cache


class AdventDay19:

    def __init__(self):
        self.data = [x for x in DayStarter(19).split('\n')]
        self._process_data()
        self._available_towls_by_char()
        self.possible_designs = []
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        desired_designes = []
        for i, x in enumerate(self.data):
            if i == 0:
                towels = [p for p in x.split(', ')]
            elif i == 1:
                pass
            elif x != '':
                desired_designes.append(x)
        self.towels = towels
        self.desired_designes = desired_designes

    def _available_towls_by_char(self):
        """Create a dictionary of towels by the first character."""
        patterns: dict[str, list] = {}
        for p in self.towels:
            if p[0] not in patterns:
                patterns[p[0]] = []
            patterns[p[0]].append(p)
        self.by_char_towels = patterns

    def find_possible_designs(self):
        """Find all possible designs that can be achieved."""
        for full_pattern in self.desired_designes:
            if self.recursive_search(full_pattern):
                self.part1 += 1
                self.possible_designs.append(full_pattern)

    def find_all_ways_for_possible_designs(self):
        """Find all ways to achieve the possible designs."""
        for pattern in self.possible_designs:
            self.part2 += self.recursive_search(pattern, 2)

    @lru_cache(maxsize=None)
    def recursive_search(self, full_pattern: str, part: int = 1) -> bool:
        """Recursively search for the desired pattern in the towels.
        If part is 1, return True if the pattern can be achieved.
        If part is 2, return the number of ways the pattern can be achieved."""
        if full_pattern == '':
            return True
        good_towels = [x for x in self.by_char_towels[full_pattern[0]]
                       if full_pattern.startswith(x)]
        if part == 1:
            return any([self.recursive_search(full_pattern[len(x):])
                        for x in good_towels])
        return sum([self.recursive_search(full_pattern[len(x):], 2)
                    for x in good_towels])


if __name__ == '__main__':
    day19 = AdventDay19()
    day19.find_possible_designs()
    day19.find_all_ways_for_possible_designs()
    print(day19.part1, day19.part2)
