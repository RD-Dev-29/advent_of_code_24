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
        self.part1 = 0
        self.part2 = 0

    def drop_bytes(self, n):
        for _ in range(n):
            try:
                self.memory_space[self.incoming_bytes.pop()] = '#'
                self.bytes_dropped += 1
            except IndexError:
                break

    def navigate(self):

        visited = set()
        search = deque([(0, 0)])
        distance = 0

        def bfs_helper(map: dict, position, goal):
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
                    self.part1 = distance
                    return
            distance += 1

    def _process_data(self):
        self.incoming_bytes = [tuple([int(x) for x in coords.split(',')])
                               for coords in self.data][::-1]
        return self

    def _generate_map(self, mini: bool = False):
        n = 7 if mini else 71
        self.memory_space = {(i, j): '.' for i in range(n) for j in range(n)}
        return self

    def print_map(self):
        for i in range(7):
            print(''.join([self.memory_space[(i, j)] for j in range(7)]))


if __name__ == '__main__':
    day18 = AdventDay18()
    day18.drop_bytes(1024)
    day18.navigate()
    print(day18.part1, day18.part2)
