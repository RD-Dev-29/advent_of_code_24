class Guard:

    change_dir_map = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
    dir_vector = {'u': [-1, 0], 'r': [0, 1], 'd': [1, 0], 'l': [0, -1]}

    def __init__(self, start_coordinates: list[int]):
        self.init_position = start_coordinates.copy()
        self.restart_loop_tracker()
        self.main_path = set()
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
        return self.possible_move

    def accept_move(self, next_tile: str, part_1: bool = True):
        self.position = self.possible_move
        if part_1:
            self._count_if_new(next_tile == '.')
            self.track_main_path(tuple(self.position))
        else:
            return self.track_potential_loop_path(tuple(self.position))

    def _count_if_new(self, new: bool):
        self.positions_seen += new

    def restart_loop_tracker(self):
        self.position = self.init_position.copy()
        self.dir = 'u'
        self.position_visits = set([(self.position[0],
                                     self.position[1],
                                     self.dir)])
        self.in_bounds = True

    def track_main_path(self, coordinates: tuple[int]):
        if coordinates != tuple(self.init_position):
            self.main_path.add(coordinates)

    def track_potential_loop_path(self, coordinates: tuple[int]):
        cur = coordinates + tuple(self.dir)
        if cur not in self.position_visits:
            self.position_visits.add(cur)
            return False
        return True


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
                        char = 'S'
                    self.room_map[(i, j)] = char
        self.part1 = 0
        self.part2 = 0

    def get_patrol_route(self, part_1: bool = True):
        while self.guard.in_bounds:
            try:
                next_tile = self.room_map[tuple(self.guard.find_next_move())]
                if next_tile != '#':
                    loop = self.guard.accept_move(next_tile, part_1)
                    self.room_map[tuple(self.guard.position)] = '!'
                    if not part_1 and loop:
                        self.part2 += 1
                        break
                else:
                    self.guard.change_dir()
            except KeyError:
                self.guard.in_bounds = False
        if part_1:
            self.part1 = self.guard.positions_seen

    def find_potential_loops(self):
        for obstical_potential in self.guard.main_path:
            self.room_map[obstical_potential] = '#'
            self.guard.restart_loop_tracker()
            self._reset_map()
            self.get_patrol_route(part_1=False)
            self.room_map[obstical_potential] = '.'

    def _reset_map(self):
        for key, val in self.room_map.items():
            if val == '!':
                self.room_map[key] = '.'


if __name__ == '__main__':
    day6 = AdventDay6()
    day6.get_patrol_route()
    day6.find_potential_loops()
    print(day6.part1, day6.part2)
