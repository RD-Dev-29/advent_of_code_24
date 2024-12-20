from day_starter import DayStarter


class AdventDay12:

    def __init__(self):
        self.data = [x for x in DayStarter(12).split('\n') if x != '']
        self.map: dict[tuple, str] = {}
        self.regions: dict[str, list[set]] = {}
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        chars = set()
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                self.map[(i, j)] = char
                chars.add(char)
        for char in chars:
            self.regions[char] = []

    def get_regions(self):
        seen = set()

        def dfs_helper(row, col, cur_char, cur_region: set, root: bool):
            if (row, col) in seen or self.map.get((row, col), None) is None:
                return
            char = self.map[(row, col)]
            if char != cur_char:
                return
            cur_region.add((row, col))
            seen.add((row, col))
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                dfs_helper(row + i, col + j, cur_char, cur_region, False)
            if root:
                self.regions[cur_char].append(cur_region)

        for i in range(len(self.data)):
            for j in range(len(self.data[0])):
                dfs_helper(i, j, self.map[(i, j)], set(), True)

    def get_region_cost(self, region: set):
        seen = set()

        def dfs_helper(row, col):
            if (row, col) in seen:
                return 0
            elif region.isdisjoint({(row, col)}):
                return 1
            seen.add((row, col))
            return (dfs_helper(row + 1, col) + dfs_helper(row - 1, col) +
                    dfs_helper(row, col + 1) + dfs_helper(row, col - 1))
        return len(region) * dfs_helper(*(list(region)[0]))

    def get_region_discount_cost(self, region: set):

        def get_rect(region):
            for i, coor in enumerate(region):
                if i == 0:
                    t = d = coor[0]
                    left = r = coor[1]
                else:
                    t = min(t, coor[0])
                    d = max(d, coor[0])
                    left = min(left, coor[1])
                    r = max(r, coor[1])
            return [t, d, left, r]

        def region_scan(region):
            t, d, left, r = get_rect(region)
            last_top = last_bottom = last_left = last_right = False
            top_edges = 0
            bottom_edges = 0
            left_edges = 0
            right_edges = 0
            for i in range(t, d + 1):
                last_top = last_bottom = False
                for j in range(left, r + 1):
                    if (i, j) not in region:
                        last_top = last_bottom = False
                        continue
                    if (i - 1, j) not in region:
                        if not last_top:
                            top_edges += 1
                        last_top = True
                    else:
                        last_top = False
                    if (i + 1, j) not in region:
                        if not last_bottom:
                            bottom_edges += 1
                        last_bottom = True
                    else:
                        last_bottom = False
            for j in range(left, r + 1):
                last_left = last_right = False
                for i in range(t, d + 1):
                    if (i, j) not in region:
                        last_left = last_right = False
                        continue
                    if (i, j - 1) not in region:
                        if not last_left:
                            left_edges += 1
                        last_left = True
                    else:
                        last_left = False
                    if (i, j + 1) not in region:
                        if not last_right:
                            right_edges += 1
                        last_right = True
                    else:
                        last_right = False
            return top_edges + bottom_edges + left_edges + right_edges
        return len(region) * region_scan(region)

    def get_total_cost(self):
        total = 0
        for sets in self.regions.values():
            for region in sets:
                total += self.get_region_cost(region)
        self.part1 = total

    def get_discount_cost(self):
        total = 0
        for sets in self.regions.values():
            for region in sets:
                total += self.get_region_discount_cost(region)
        self.part2 = total


if __name__ == '__main__':
    day12 = AdventDay12()
    day12.get_regions()
    day12.get_total_cost()
    day12.get_discount_cost()
    print(day12.part1, day12.part2)
