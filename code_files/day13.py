from day_starter import DayStarter
import numpy as np

map_val = {0: 'A', 1: 'B', 2: 'G'}


class AdventDay13:

    def __init__(self):
        self.data = [x for x in DayStarter(13).split('\n') if x != '']
        self._process_data()
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
        self.machines: list[dict[str, list[int]]] = machines

    def get_token_cost(self, part: str = 'part_1'):
        for machine in self.machines:
            if part == 'part_1':
                self.part1 += self._check_machine(machine, part)
            else:
                machine['G'] = [x + 10000000000000 for x in machine['G']]
                self.part2 += self._check_machine(machine, part)

    def _check_machine(self, machine, part: str = 'part_1'):
        A = np.array([[machine['A'][0], machine['B'][0]],
                      [machine['A'][1], machine['B'][1]]])
        b = np.array([machine['G'][0], machine['G'][1]])
        ans = np.rint(np.linalg.solve(A, b))
        if any([x < 0 for x in ans]):
            return 0
        if part == 'part_1' and any([x > 100 for x in ans]):
            return 0
        if (A @ ans == b).all():
            return ans[0] * 3 + ans[1]
        return 0


if __name__ == '__main__':
    day13 = AdventDay13()
    day13.get_token_cost()
    day13.get_token_cost('part_2')
    print(day13.part1, day13.part2)
