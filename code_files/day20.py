from day_starter import DayStarter


class AdventDay20:

    def __init__(self):
        self.data = [x for x in DayStarter(20).split()]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        race_map = {}
        for i, line in enumerate(self.data):
            for j, char in enumerate(line):
                race_map[(i, j)] = char
                if char == 'S':
                    self.start = (i, j)
                elif char == 'E':
                    self.end = (i, j)
        self.n, self.m = i, j
        self.race_map = race_map

    def traverse_map(self):

        self.tile_scores = {}
        cur_pos = self.start
        cur_score = 0

        while cur_pos != self.end:
            self.tile_scores[cur_score] = cur_pos
            self.race_map[cur_pos] = cur_score
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (cur_pos[0] + i, cur_pos[1] + j)
                if self.race_map.get(new_pos, 'X') == '.' or\
                        self.race_map.get(new_pos, 'X') == 'E':
                    cur_pos = new_pos
                    cur_score += 1
                    break
        self.tile_scores[cur_score] = cur_pos
        self.race_map[cur_pos] = cur_score

    def allow_2_pico_cheat(self, improvement_goal=101):
        for score in range(self.race_map[self.end]):
            score_i_position = self.tile_scores[score]
            for i, j in [(0, 2), (0, -2), (2, 0), (-2, 0)]:
                new = (score_i_position[0] + i, score_i_position[1] + j)
                race_map_jump = self.race_map.get(new, 'X')
                if isinstance(race_map_jump, int) and\
                        race_map_jump - score >= improvement_goal:
                    self.part1 += 1


if __name__ == '__main__':
    day20 = AdventDay20()
    print(day20.data)
    day20.traverse_map()
    day20.allow_2_pico_cheat()
    print(day20.part1, day20.part2)
