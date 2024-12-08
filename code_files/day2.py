"""Day 2 of Advent of Code 2024.

The goal of part 1 is to find the number of rows in the input file that are
"safe". A row is considered safe if the absolute difference between each
integer in the row is less than or equal to 3 and that any row is monotonicly
increasing or decreasing.

We can use a set to store the differences
between each integer in the row and check if the set is a subset of the set of
differences that are less strictly between 1 and 3 in a monotonic direction.

The goal of part 2 is to find the number of rows in the input file that are
"safe" and to allow for one integer in the row to be removed to make the row
"safe". We can use the same method as part 1 to find the safe rows and then
iterate over the rows that are not safe to see if removing one integer makes
the row safe.
"""


class AdventDay2:

    def __init__(self):
        """Read in the input file and store the data in a list of lists."""
        self.data = []
        self.unsafe = []
        with open('input_files/day2input.txt', 'r') as f:
            for line in f.readlines():
                self.data.append([int(x) for x in line.split()])
        self.part1 = 0
        self.part2 = 0

    def find_safe_reports(self):
        """Find the number of safe rows in the input file and also stores
        any unsafe row's index in a list for part 2."""
        for i, row in enumerate(self.data):
            if self._is_safe_row(row):
                self.part1 += 1
                self.part2 += 1
            else:
                self.unsafe.append(i)

    def allow_one_bad_level(self):
        """Iterate over the unsafe rows and check if removing one integer
        makes the row safe."""
        for index in self.unsafe:
            row = self.data[index]
            for i in range(len(row)):
                if self._is_safe_row(row[:i] + row[i+1:]):
                    self.part2 += 1
                    break

    def _is_safe_row(self, row):
        """Check if the row is safe by checking if the absolute difference
        between each integer in the row is less than or equal to 3 and that
        the row is monotonicly increasing or decreasing."""
        self.row_diff_set = {row[j] - row[j-1] for j in range(1, len(row))}
        return (self.row_diff_set <= {1, 2, 3} or
                self.row_diff_set <= {-1, -2, -3})


if __name__ == '__main__':
    mgr = AdventDay2()
    mgr.find_safe_reports()
    mgr.allow_one_bad_level()
    print(mgr.part1, mgr.part2)
