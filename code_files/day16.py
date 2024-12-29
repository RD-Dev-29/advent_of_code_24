from day_starter import DayStarter
from collections import deque
from math import inf

dir_map = {
    'u': {'v': (-1, 0), 'turns': ['l', 'r']},
    'd': {'v': (1, 0), 'turns': ['l', 'r']},
    'l': {'v': (0, -1), 'turns': ['u', 'd']},
    'r': {'v': (0, 1), 'turns': ['u', 'd']}
}


class AdventDay16:

    def __init__(self):
        self.data = [x for x in DayStarter(16).split()]
        with open('input_files/day16input_mini.txt') as f:
            self.data = f.read().split('\n')
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
                    maze[(i, j)] = char
                    self.end = (i, j)
                else:
                    maze[(i, j)] = char
        self.maze = maze

    def traverse_maze(self):
        best_score = [inf]
        future_moves = deque()
        seen = set()

        def dfs(maze, coords, score, dir):
            if maze[coords] == '.':
                maze[coords] = score
            elif coords in seen and maze[coords] <= score:
                return
            elif maze[coords] == '#':
                return
            elif maze[coords] == 'E':
                best_score[0] = min(best_score[0], score)
                return
            
            elif maze[coords] > score or coords not in seen:
                maze[coords] = score
            seen.add(coords)
            forward = (coords[0] + dir_map[dir]['v'][0],
                       coords[1] + dir_map[dir]['v'][1])
            future_moves.append([maze, forward, score + 1, dir])
            for next_dir in dir_map[dir]['turns']:
                next_coords = (coords[0] + dir_map[next_dir]['v'][0],
                               coords[1] + dir_map[next_dir]['v'][1])
                future_moves.append([maze, next_coords, score + 1001, next_dir])
        future_moves.append([self.maze, self.start, 0, 'r'])
        while future_moves:
            maze, coords, score, dir = future_moves.popleft()
            dfs(maze, coords, score, dir)
        self.part1 = best_score[0]

    def reverse_maze(self):
        action_spots = []

        def dfs(maze, coords, last_score, dir):
            if isinstance(maze[coords], str):
                return
            elif isinstance(maze[coords], int):
                if maze[coords] >= last_score:
                    return
                action_spots.append(coords)
                old_score = maze[coords]
                maze[coords] = 'O'
                next_coords = (coords[0] + dir_map[dir]['v'][0],
                               coords[1] + dir_map[dir]['v'][1])
                dfs(maze, next_coords, old_score, dir)
                for next_dir in dir_map[dir]['turns']:
                    next_coords = (coords[0] + dir_map[next_dir]['v'][0],
                                   coords[1] + dir_map[next_dir]['v'][1])
                    dfs(maze, next_coords, old_score, next_dir)
        down = (self.end[0] + 1, self.end[1])
        left = (self.end[0], self.end[1] - 1)
        dfs(self.maze, down, self.part1, 'd')
        dfs(self.maze, left, self.part1, 'l')

        self.part2 = len(action_spots)

    def print_maze(self):
        for i in range(self.m):
            for j in range(self.n):
                extra = ' '*(6-len(str(self.maze[(i, j)])))
                print(str(self.maze[(i, j)])+extra, end=' ')
            print()
        print('\n')


if __name__ == '__main__':
    day16 = AdventDay16()
    day16.traverse_maze()
    day16.print_maze()
    day16.reverse_maze()
    day16.print_maze()
    print(day16.part1, day16.part2)
