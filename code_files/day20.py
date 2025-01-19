""" Day 20 of Advent of Code 2024

The goal of day 20 is to find shorter paths in a race. The race map is a grid
of walls and empty spaces, with a start and end point. The main maze has only
one path from start to end, but walls are allowed to be ignored for varying
amounts of time or moves. The goal is to find distinct shortcuts (activation to
ending time) that result in savings of at least 100 steps or 100 picoseconds.

In part 1, the goal is to find all the paths that are at least 100 steps
shorter than the main path if you are allowed to ignore walls and then remain
on the main path in two moves (aka skip one wall and end on the main path).

In part 2, the goal is to find all the paths that are
at least 100 steps shorter than the main path if you are allowed to ignore
walls and then continue on the main path in 20 moves.

Moves in the maze are limited to up, down, left, and right and one move is
reffered to as one picosecond.
"""

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
        """Traverse the original map obeying all walls and assign scores to
        each tile based on the distance from the start."""

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

    def allow_n_pico_cheat(self, improvement_goal=100, cheat_allowed=2,
                           part: int = 1):
        """Allow the player to cheat by ignoring walls and jumping to any
        tile that is at most n picoseconds away from the current tile. Then
        check if the player can reach the end of the maze in at least
        improvement_goal fewer steps."""
        shifts = self._n_pico_cheat_map(cheat_allowed)

        # Iterate through all the tiles that are at least improvement_goal
        # steps away from the end of the maze.
        for score in range(self.race_map[self.end] - improvement_goal):
            score_i_position = self.tile_scores[score]

            # Iterate through all the possible shifts that can be made in
            # cheat_allowed picoseconds.
            for i, j in shifts:
                new = (score_i_position[0] + i, score_i_position[1] + j)
                race_map_jump = self.race_map.get(new, 'X')

                # If the possible shift does not end on the main path, skip it.
                if not isinstance(race_map_jump, int):
                    continue

                # If the possible shift ends on the main path, check if the
                # player can reach the end of the maze in at least
                # improvement_goal fewer steps. Also accounting for the
                # picoseconds used to make the shift.
                if race_map_jump - score - abs(i) - abs(j) >= improvement_goal:
                    if part == 1:
                        self.part1 += 1
                    else:
                        self.part2 += 1

    def _n_pico_cheat_map(self, n: int):
        """Return a list of all possible shifts that can be made in n
        picoseconds."""
        shifts = []
        for i in range(-n, n + 1):
            for j in range(-n, n + 1):
                if abs(i) + abs(j) <= n and abs(i) + abs(j) > 1:
                    shifts.append((i, j))
        return shifts


if __name__ == '__main__':
    day20 = AdventDay20()
    day20.traverse_map()
    day20.allow_n_pico_cheat()
    day20.allow_n_pico_cheat(100, 20, 2)
    print(day20.part1, day20.part2)
