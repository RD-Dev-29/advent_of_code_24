from day_starter import DayStarter


class AdventDay10:

    def __init__(self):
        self.data = [x for x in DayStarter(10).split('\n') if x != '']
        self.map_data = {}
        self.trail_heads = []
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        for i, line in enumerate(self.data):
            for j, val in enumerate(line):
                self.map_data[(i, j)] = int(val)
                if int(val) == 0:
                    self.trail_heads.append((i, j))

    def get_trailhead_metrics(self):
        for head in self.trail_heads:
            self._find_trailhead_metric(*head, 'part1')
            self._find_trailhead_metric(*head, 'part2')

    def _find_trailhead_metric(self, row: int, col: int, part: str):
        if part == 'part1':
            peaks = set()

        def dfs_helper(row, col, cur_val):
            try:
                new_val = self.map_data[(row, col)]
            except KeyError:
                return 0
            if new_val == 9 and cur_val == 8:
                if part == 'part1' and (row, col) not in peaks:
                    peaks.add((row, col))
                    return 1
                elif part == 'part2':
                    return 1
                return 0
            elif new_val - 1 == cur_val:
                return (dfs_helper(row + 1, col, new_val) +
                        dfs_helper(row - 1, col, new_val) +
                        dfs_helper(row, col - 1, new_val) +
                        dfs_helper(row, col + 1, new_val))
            return 0

        if part == 'part1':
            self.part1 += dfs_helper(row, col, -1)
        else:
            self.part2 += dfs_helper(row, col, -1)


if __name__ == '__main__':
    day10 = AdventDay10()
    day10.get_trailhead_metrics()
    print(day10.part1, day10.part2)
