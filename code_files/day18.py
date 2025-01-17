""" Day 18 of Advent of Code 2024.

The goal is to navigate a memory space to reach a goal. The memory space is
a grid of '.' and '#' characters. The goal is to reach the bottom-right
corner of the grid. The memory space is initially open, but bytes are dropped
into spaces as specified in the input.

The goal of part 1 is to determine the shortest path to the goal after 1024
bytes are dropped. The goal of part 2 is to determine the last byte dropped
before the path to the goal is blocked.
"""

from day_starter import DayStarter
from collections import deque


class AdventDay18:

    def __init__(self, mini: bool = False):
        self.data = [x for x in DayStarter(18).split()]
        if mini:
            with open('input_files/day18input_micro.txt') as f:
                self.data = [x for x in f.read().split('\n') if x != '']
        self._process_data()._generate_map(mini)
        self.goal = (6, 6) if mini else (70, 70)
        self.bytes_dropped = 0
        self.last_byte = None
        self.part1 = 0
        self.part2 = 0

    def drop_bytes(self, n: int):
        """Drop n bytes into the memory space. Terminates if no remaining
        bytes.

        Args:
            n: int, number of bytes to drop.
        """
        for _ in range(n):
            try:
                position = self.incoming_bytes.pop()
                self.last_byte = position
                self.memory_space[position] = '#'
                self.bytes_dropped += 1
            except IndexError:
                break

    def determine_block(self):
        """Determines the byte which is the last to be dropped before the
        path to the goal is blocked."""
        while True:
            self.drop_bytes(1)
            if self.navigate(part1=False):
                break
        self.part2 = self.last_byte

    def navigate(self, part1: bool = True):
        """Navigate from (0, 0) to the goal, updating the distance to the goal
        in self.part1. If part1 is False, return True if no path is found."""

        visited = set()
        search = deque([(0, 0)])
        distance = 0

        def bfs_helper(map: dict, position, goal):
            """Helper function for breadth-first search. Returns True if the
            goal is reached, False or None otherwise."""
            if position in visited or map.get(position, 'N') in 'N#':
                return False
            if position == goal:
                return True
            visited.add(position)
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_position = tuple([sum(x) for x in
                                      zip(position, direction)])
                search.append(new_position)

        while search:
            for _ in range(len(search)):
                next_spot = search.popleft()
                if bfs_helper(self.memory_space, next_spot, self.goal):
                    if part1:
                        self.part1 = distance
                    return
            distance += 1

        return True  # no path found

    def _process_data(self):
        """Process the data into a list of tuples of coordinates."""
        self.incoming_bytes = [tuple([int(x) for x in coords.split(',')])
                               for coords in self.data][::-1]
        return self

    def _generate_map(self, mini: bool = False):
        """Generate a map of the memory space."""
        n = 7 if mini else 71
        self.memory_space = {(i, j): '.' for i in range(n) for j in range(n)}
        return self

    def print_map(self):
        """Print the memory space."""
        for i in range(self.goal[0] + 1):
            print(''.join([self.memory_space[(i, j)]
                           for j in range(self.goal[1] + 1)]))


if __name__ == '__main__':
    day18 = AdventDay18()
    day18.drop_bytes(1024)
    day18.navigate()
    day18.determine_block()
    print(day18.part1, day18.part2)
