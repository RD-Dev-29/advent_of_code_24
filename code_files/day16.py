from day_starter import DayStarter
from collections import deque

dir_map = {
    'u': {'v': (-1, 0), 't': ['l', 'r']}, 'd': {'v': (1, 0), 't': ['l', 'r']},
    'l': {'v': (0, -1), 't': ['u', 'd']}, 'r': {'v': (0, 1), 't': ['u', 'd']}
}


class AdventDay16:

    def __init__(self):
        self.data = [x for x in DayStarter(16).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.m = len(self.data)
        self.n = len(self.data[0])
        maze = {}
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                if char == 'S':
                    maze[(i, j)] = 0
                    self.start = (i, j)
                elif char == 'E':
                    maze[(i, j)] = 1000000000000
                    self.end = (i, j)
                else:
                    maze[(i, j)] = char
        self.maze = maze

    def traverse_maze(self):
        future_moves, good_spots, maze = deque(), set(), self.maze

        def dfs(loc, score, dir, reverse):
            if maze[loc] == '#' or (isinstance(maze[loc], int) and
                                    maze[loc] < score and not reverse):
                return
            if maze[loc] == '.' or maze[loc] > score:
                if reverse:
                    return
                maze[loc] = score
            if reverse:
                good_spots.add(loc)
            for n_dr in [dir, *dir_map[dir]['t']]:
                n_loc = tuple([loc[i] + dir_map[n_dr]['v'][i] for i in [0, 1]])
                dif = (1001 if n_dr != dir else 1) * (-1 if reverse else 1)
                future_moves.append([n_loc, score + dif, n_dr, reverse])

        future_moves.append([self.start, 0, 'r', False])
        while future_moves:
            dfs(*future_moves.popleft())
        future_moves.append([self.end, maze[self.end], 'd', True])
        future_moves.append([self.end, maze[self.end], 'l', True])
        while future_moves:
            dfs(*future_moves.popleft())
        self.part1, self.part2 = maze[self.end], len(good_spots)


if __name__ == '__main__':
    day16 = AdventDay16()
    day16.traverse_maze()
    print(day16.part1, day16.part2)
