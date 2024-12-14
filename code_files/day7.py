"""Day 7 of Advent of Code 2024.

The goal of part 1 is to find if certain operations can be placed between
numbers in a list to get a certain result. The operations are addition and
multiplication. We can iterate over the list of numbers and try all possible
combinations of operations to see if the result matches the target.

The goal of part 2 is to find if certain operations can be placed between
numbers in a list to get a certain result. The operations are addition,
multiplication, and concatenation. We can iterate over the list of numbers
and try all possible combinations of operations to see if the result matches
the target.
"""

from itertools import product


class AdventDay7:

    def __init__(self):
        self.calibrations = []
        self.invalid_in_part1 = []
        with open('input_files/day7input.txt', 'r') as f:
            for line in f.readlines():
                temp = line.split(': ')
                temp[0] = int(temp[0])
                temp[1] = [int(x) for x in temp[1].split(' ')]
                self.calibrations.append(temp)
        self.part1 = 0
        self.part2 = 0

    def place_operators(self, part: str):
        """Place the operators between the numbers in the calibration list to
        get the target value."""
        ops = [0, 1] if part == 'part1' else [0, 1, 2]
        cals = self.calibrations if part == 'part1' else self.invalid_in_part1
        for cal in cals:
            found = False
            for choice in product(ops, repeat=len(cal[1])-1):
                if cal[0] == self.use_choice(cal[1], choice, cal[0]):
                    self.part1 += cal[0] if part == 'part1' else 0
                    self.part2 += cal[0]
                    found = True
                    break
            if not found and part == 'part1':
                self.invalid_in_part1.append(cal)

    def use_choice(self, cal_list: list[int], choice: int, goal: int):
        """Use the choice of operators to calculate the result of the
        calibration list."""
        temp = cal_list[0]
        for i, val in enumerate(choice):
            if val == 0:
                temp += cal_list[i + 1]
            elif val == 1:
                temp *= cal_list[i + 1]
            else:
                temp = int(str(temp) + str(cal_list[i + 1]))
            if temp > goal:
                break
        return temp


if __name__ == '__main__':
    day7 = AdventDay7()
    day7.place_operators('part1')
    day7.place_operators('part2')
    print(day7.part1, day7.part2)
