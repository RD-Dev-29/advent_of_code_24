from day_starter import DayStarter


class Robot:

    move_map = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

    def __init__(self, coords: list):
        self.coords = coords
        self.temp = None
        self.prior = coords

    def attempt_move(self, dir, map: dict):
        self.temp =\
            tuple([self.coords[i] + self.move_map[dir][i] for i in range(2)])
        if map[self.temp] == '#':
            return False
        elif map[self.temp] == '.':
            return True
        elif isinstance(map[self.temp], Box):
            return map[self.temp].complete_move(dir, map)

    def complete_move(self, dir, map):
        if self.attempt_move(dir, map):
            self.prior = [x for x in self.coords]
            self.coords = [x for x in self.temp]
            self.temp = None
            self.update_map(map)
            return True
        self.temp = None
        return False

    def update_map(self, map):
        map[tuple(self.coords)] = self
        map[tuple(self.prior)] = '.'

    def __str__(self) -> str:
        return '@'


class Box(Robot):

    def __str__(self) -> str:
        return 'O'


class AdventDay15:

    def __init__(self):
        self.data = [x for x in DayStarter(15).split()]
        # with open('input_files/day15input_micro.txt') as f:
        #     self.data = f.read().split()
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.boxes: list[Box] = []
        self.m = 0
        self.moves = ''
        warehouse_map = {}
        for i, line in enumerate(self.data):
            if '<' in line or '>' in line or '^' in line or 'v' in line:
                self.moves += line.split()[0]
                continue
            if '#' in line:
                self.m += 1
                self.n = len(line)
            for j, char in enumerate(line):
                if char in ['.', '#']:
                    warehouse_map[(i, j)] = char
                elif char == 'O':
                    warehouse_map[(i, j)] = Box([i, j])
                    self.boxes.append(warehouse_map[(i, j)])
                elif char == '@':
                    warehouse_map[(i, j)] = '@'
                    self.robot = Robot([i, j])
        self.warehouse_map = warehouse_map

    def execute_moves(self):
        for move in self.moves:
            self.robot.complete_move(move, self.warehouse_map)
            # self.print_map()

    def calc_score(self):
        self.part1 = 0
        for box in self.boxes:
            self.part1 += box.coords[0]*100 + box.coords[1]

    def print_map(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.warehouse_map[(i, j)], end='')
            print()


if __name__ == '__main__':
    day15 = AdventDay15()
    day15.execute_moves()
    day15.calc_score()
    print(day15.part1, day15.part2)
