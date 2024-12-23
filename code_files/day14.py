from day_starter import DayStarter
import regex as re


class AdventDay14:

    def __init__(self):
        self.data = DayStarter(14)
        self._process_data()
        self.map_size = [101, 103]
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        robots = []
        robot = {}
        for pair in re.findall(r'\-?\d+,\-?\d+', self.data):
            robot['p' if len(robot) == 0 else 'v'] =\
                [int(x) for x in pair.split(',')]
            if len(robot) == 2:
                robots.append(robot)
                robot = {}
        self.robots = robots

    def move_robots(self, seconds):
        for robot in self.robots:
            self.move_robot(robot, seconds)
        self.part1 = self.get_safety_score()
        for robot in self.robots:
            self.move_robot(robot, -seconds)

    def move_robot(self, robot: dict, seconds):
        for i in range(2):
            robot['p'][i] =\
                (robot['p'][i] + robot['v'][i]*seconds) % self.map_size[i]
        return robot

    def calculate_christmas_tree(self):
        for i in range(10000):
            for bot in self.robots:
                self.move_robot(bot, 1)
            if self.check_symmetry():
                self.part2 = i + 1
                self.print_map()
                return

    def check_symmetry(self):
        map = [[' ' for _ in range(self.map_size[0])]
               for _ in range(self.map_size[1])]
        for robot in self.robots:
            map[robot['p'][1]][robot['p'][0]] = '#'
        for row in map:
            temp = ''.join(row)
            if '##############' in temp:
                return True
        return False

    def get_safety_score(self):
        quads = [0, 0, 0, 0]
        for robot in self.robots:
            if (robot['p'][0] < self.map_size[0] // 2 and
                    robot['p'][1] < self.map_size[1] // 2):
                quads[0] += 1
            elif (robot['p'][0] > self.map_size[0] // 2 and
                  robot['p'][1] < self.map_size[1] // 2):
                quads[1] += 1
            elif (robot['p'][0] < self.map_size[0] // 2 and
                  robot['p'][1] > self.map_size[1] // 2):
                quads[2] += 1
            elif (robot['p'][0] > self.map_size[0] // 2 and
                  robot['p'][1] > self.map_size[1] // 2):
                quads[3] += 1
        return quads[0] * quads[1] * quads[2] * quads[3]

    def print_map(self):
        map = [[' ' for _ in range(self.map_size[0])]
               for _ in range(self.map_size[1])]
        for robot in self.robots:
            map[robot['p'][1]][robot['p'][0]] = '#'
        for row in map:
            print(''.join(row))


if __name__ == '__main__':
    day14 = AdventDay14()
    day14.move_robots(100)
    day14.calculate_christmas_tree()
    print(day14.part1, day14.part2)
