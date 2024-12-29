from day_starter import DayStarter

old = []
stack = []
move_map = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}


class Robot:

    def __init__(self, coords: tuple[int]):
        self.coords = coords


class AdventDay15:

    def __init__(self):
        self.data = [x for x in DayStarter(15).split()]
        self.part1 = 0
        self.part2 = 0

    def process_data(self, part: int = 1):
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
                    warehouse_map[(i, j*part)] = char if part == 1 else '['
                    warehouse_map[(i, part*(j+1) - 1)] =\
                        char if part == 1 else ']'
                elif char == '@':
                    self.robot = Robot((i, j*part))
                    warehouse_map[(i, j*part)] = '@'
                    if part == 2:
                        warehouse_map[(i, part*(j+1) - 1)] = '.'
        self.warehouse_map = warehouse_map

    def execute_moves(self):
        for move in self.moves:
            if self.attempt_move(self.robot.coords, move, '@'):
                for coord in old:
                    self.warehouse_map[coord] = '.'
                for coord in stack:
                    self.warehouse_map[coord[0]] = coord[1]
                self.robot.coords = stack[0][0]
            stack.clear()
            old.clear()

    def attempt_move(self, cur, dir, char):
        temp = tuple([cur[i] + move_map[dir][i] for i in range(2)])
        old.append(cur)
        stack.append([temp, char])
        if self.warehouse_map[temp] == '#':
            return False
        elif self.warehouse_map[temp] == '.':
            return True
        elif self.warehouse_map[temp] == 'O':
            return self.attempt_move(temp, dir, 'O')
        elif self.warehouse_map[temp] in '[]' and dir in '><':
            return self.attempt_move(temp, dir, self.warehouse_map[temp])
        elif self.warehouse_map[temp] == '[' and dir in '^v':
            return (self.attempt_move(temp, dir, '[') &
                    self.attempt_move((temp[0], temp[1] + 1), dir, ']'))
        return (self.attempt_move(temp, dir, ']') &
                self.attempt_move((temp[0], temp[1] - 1), dir, '['))

    def calc_score(self, part: int = 1):
        for key, val in self.warehouse_map.items():
            if val in '[O':
                if part == 1:
                    self.part1 += key[0]*100 + key[1]
                else:
                    self.part2 += key[0]*100 + key[1]


if __name__ == '__main__':
    day15 = AdventDay15()
    day15.process_data()
    day15.execute_moves()
    day15.calc_score()
    day15.process_data(2)
    day15.execute_moves()
    day15.calc_score(2)
    print(day15.part1, day15.part2)
