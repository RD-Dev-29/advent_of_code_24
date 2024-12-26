from day_starter import DayStarter
from typing import Union


class Robot:

    move_map = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

    def __init__(self, coords: list[list]):
        self.coords = coords
        self.temp = None
        self.prior = coords

    def attempt_move(self, dir, map: dict[tuple[int, int],
                                          Union[str, 'Robot']]):
        self.temp =\
            [tuple([coord[i] + self.move_map[dir][i]
                   for i in range(2)])
                for coord in self.coords]
        if any([map[self.temp[i]] == '#' for i in range(len(self.temp))]):
            return False

        def final_check(temp):
            if map[temp] == '.':
                return True
            elif map[temp] == self:
                return True
            elif isinstance(map[temp], Box):
                return map[temp].complete_move(dir, map)

        return all([final_check(self.temp[i]) for i in range(len(self.temp))])

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
        for i in range(len(self.coords)):
            print(self.coords[i])
            map[tuple(self.coords[i])] = self
            map[tuple(self.prior[i])] = '.'

    def __str__(self) -> str:
        return '@'


class Box(Robot):

    def __str__(self) -> str:
        if len(self.coords) == 1:
            return 'O'
        elif len(self.coords) == 2:
            return '['


class AdventDay15:

    def __init__(self):
        self.data = [x for x in DayStarter(15).split()]
        with open('input_files/day15input_mini.txt') as f:
            self.data = f.read().split()
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self, part: int = 1):
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
                self.n = len(line*part)
            for j, char in enumerate(line):
                if char in ['.', '#']:
                    warehouse_map[(i, j*part)] = char
                    warehouse_map[(i, part*(j+1) - 1)] = char
                elif char == 'O':
                    box = Box(list(set([(i, j*part),
                                        (i, part*(j+1) - 1)])))
                    for coord in box.coords:
                        warehouse_map[coord] = box
                    self.boxes.append(box)
                elif char == '@':
                    warehouse_map[(i, j*part)] = '@'
                    warehouse_map[(i, part*(j+1) - 1)] =\
                        '.' if part == 2 else '@'
                    self.robot = Robot([[i, j*part]])
        self.warehouse_map = warehouse_map

    def execute_moves(self):
        for i, move in enumerate(self.moves):
            self.robot.complete_move(move, self.warehouse_map)
            print(move)
            self.print_map()
            # self.print_map()

    def calc_score(self, part: int = 1):
        if part == 1:
            for box in self.boxes:
                self.part1 += box.coords[0][0]*100 + box.coords[0][1]
        for box in self.boxes:
            self.part2 += box.coords[0][0]*100 + box.coords[0][1]

    def print_map(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.warehouse_map[(i, j)], end='')
            print()


if __name__ == '__main__':
    day15 = AdventDay15()
    # day15.print_map()
    # day15.execute_moves()
    # day15.calc_score()
    day15._process_data(2)
    day15.execute_moves()
    day15.calc_score(2)
    print(day15.part1, day15.part2)
