from day_starter import DayStarter

map_val = {0: 'A', 1: 'B', 2: 'G'}


class AdventDay13:

    def __init__(self):
        self.data = [x for x in DayStarter(13).split('\n') if x != '']
        with open('input_files/day13input_micro.txt') as f:
            self.data = [x for x in f.read().split('\n') if x != '']
        self.machines: list[dict[str, list[int]]] = []
        self._process_data()
        print(len(self.machines))
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        machines = []
        i = 0
        cur_machine = {}
        for line in self.data:
            cur_machine[map_val[i]] =\
                list(map(int, [x.split('+' if i < 2 else '=')[1] for x in
                               line.split(':')[1].split(',')]))
            if i == 2:
                machines.append(cur_machine)
                cur_machine = {}
            i = (i + 1) % 3
        self.machines = machines

    def get_token_cost(self, part: str = 'part1'):
        if part == 'part2':
            self.get_b_goals()
            for i, machine in enumerate(self.machines):
                print(i)
                self.part2 += self.check_machine(machine, 'part2')
        for machine in self.machines:
            self.part1 += self.check_machine(machine)

    def get_b_goals(self):
        for machine in self.machines:
            machine['G'] = [x + 10000000000000 for x in machine['G']]

    def check_machine(self, machine, part: str = 'part1'):
        b_presses = self._get_div_b(*machine['G'], *machine['B'], part)
        a_presses = 0
        start = [x * b_presses for x in machine['B']]
        while start != machine['G']:
            print(start, machine['G'], b_presses, a_presses)
            if part == 'part1' and a_presses > 100:
                return 0
            if part == 'part2' and b_presses < 0:
                return 0
            if start[0] < machine['G'][0] or start[1] < machine['G'][1]:
                a_presses += 1
                start[0] += machine['A'][0]
                start[1] += machine['A'][1]
            elif start[0] > machine['G'][0] or start[1] > machine['G'][1]:
                start[0] -= machine['B'][0]
                start[1] -= machine['B'][1]
                b_presses -= 1
        return a_presses * 3 + b_presses

    def _get_div_b(self, goal_x, goal_y, b_x, b_y, part: str = 'part1'):
        a = goal_x // b_x
        b = goal_y // b_y
        if part == 'part1':
            return min(a, b, 100)
        return min(a, b)


if __name__ == '__main__':
    day13 = AdventDay13()
    day13.get_token_cost()
    day13.get_token_cost('part2')
    print(day13.part1, day13.part2)
