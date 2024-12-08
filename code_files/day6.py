class Guard:

    change_dir_map = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}

    dir_vector = {'u': [-1, 0], 'r': [0, 1], 'd': [1, 0], 'l': [0, -1]}

    def __init__(self, start_coordinates: list[int], dir: str = 'u'):
        self.position = start_coordinates
        self.init_position = start_coordinates.copy()
        self.dir = dir
        self.positions_seen = 1
        self.possible_move = None
        self.in_bounds = True

    def change_dir(self):
        self.dir = self.change_dir_map[self.dir]

    def find_next_move(self):
        new = [0, 0]
        for x in range(2):
            new[x] = self.position[x] + self.dir_vector[self.dir][x]
        self.possible_move = new

    def accept_move(self, val: str):
        self.position = self.possible_move
        self._count_if_new(val == '.')

    def _count_if_new(self, new: bool):
        self.positions_seen += new


class AdventDay6:

    def __init__(self):
        self.room_map = {}
        with open('input_files/day6input.txt', 'r') as f:
            for i, line in enumerate(f.readlines()):
                for j, char in enumerate(line):
                    if char == '\n':
                        continue
                    if char == '^':
                        self.guard = Guard([i, j])
                        char = '!'
                    self.room_map[(i, j)] = char
        self.part1 = 0
        self.part2 = 0

    def get_patrol_route(self):
        while self.guard.in_bounds:
            self.guard.find_next_move()
            try:
                map_val = self.room_map[tuple(self.guard.possible_move)]
                if map_val != '#':
                    self.guard.accept_move(map_val)
                    self.room_map[tuple(self.guard.position)] = '!'
                else:
                    self.guard.change_dir()
            except KeyError:
                self.guard.in_bounds = False
        self.part1 = self.guard.positions_seen


if __name__ == '__main__':
    day6 = AdventDay6()
    day6.get_patrol_route()
    print(day6.part1, day6.guard.position, day6.guard.init_position)
