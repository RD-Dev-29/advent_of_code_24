"""Day 5 of Advent of Code 2024.

The goal of part 1 is to find the sum of the middle number in each update
that is valid according to the sorting rules. The rules have been provided
as a list of pairs of numbers where the first number must come before the
second number in the update. We can iterate over the updates and check if
the update is valid according to the rules.

The goal of part 2 is to find the sum of the middle number in each update
that is invalid according to the sorting rules once the update has been
fixed. We can iterate over the invalid updates and swap the numbers in the
update until the update is valid according to the rules.
"""


class AdventDay5:

    def __init__(self):
        """Initialize the rules and updates for the sorting system. The rules
        are stored as a dictionary where the key is the first number in the
        rule and the value is the set of numbers that must come after the key.

        The updates are stored as a list of lists."""
        self.rules: dict[int, set] = {}
        self.updates = []
        self.bad_updates = []
        with open('input_files/day5input.txt', 'r') as f:
            for line in f.readlines():
                if '|' in line:
                    self._process_rule(self._process_line(line, '|'))
                elif line == '\n':
                    pass
                else:
                    self.updates.append(self._process_line(line, ','))
        self.sort_order = self.fix_update(list(self.rules.keys()))
        self.part1 = 0
        self.part2 = 0

    def check_updates(self):
        """Check the updates to find the sum of the middle number in each
        update that is valid according to the rules."""
        for update in self.updates:
            if self._validate_update(update):
                self.part1 += update[len(update)//2]

    def fix_bad_updates(self):
        """Fixes the bad updates and finds the sum of the middle number in
        update."""
        for update in self.bad_updates:
            self.fix_update(update)
            self.part2 += update[len(update)//2]

    def _validate_update(self, update: list[int]):
        """Check if the update is valid according to the rules.

        Args:
            update (list[int]): The update to check."""
        good = True
        for i in range(len(update) - 1, 0, -1):
            if not self.rules[update[i]].isdisjoint(set(update[:i])):
                good = False
                self.bad_updates.append(update)
                break
        return good

    def fix_update(self, update: list[int]):
        """Fix the update by swapping the numbers until the update is valid.

        Args:
            update (list[int]): The update to fix."""
        l, r = 0, 1
        while r < len(update):
            if self.rules[update[r]].intersection(set([update[l]])):
                update[l], update[r] = update[r], update[l]
            r += 1
            if r == len(update):
                l += 1
                r = l + 1
        return update

    def _process_rule(self, item: list[int]):
        """Process the rule and add it to the rules dictionary.

        Args:
            item (list[int]): The rule to process."""
        try:
            self.rules[item[0]].add(item[1])
        except KeyError:
            self.rules[item[0]] = set([item[1]])

    def _process_line(self, string_list: str, on: str):
        """Process the line and return the list of integers."""
        return [int(x) for x in string_list.replace('\n', '').split(on)]


if __name__ == '__main__':
    day5 = AdventDay5()
    day5.check_updates()
    day5.fix_bad_updates()
    print(day5.part1, day5.part2)
