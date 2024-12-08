"""Day 1 of Advent of Code 2024.
The goal of part 1 is to find the sum of the absolute differences between the
two lists of integers after the lists have been sorted from least to greatest.

The goal of part 2 is to find the sum of each integer in the first list
multiplied by the count of its appearance in the second list. By using
dictionaries as counters, we can quickly multiply each unique integer in the
left list by it's occurance in the left list and the right list to not make
repeated calls to the right lists dictionary count.
"""


class AdventDay1:

    def __init__(self):
        """Read in the input file and sort the two lists and create counters.
        The counters will be used to multiply the integer by the count of its
        appearance in each list."""
        self.left = []
        self.right = []
        with open('input_files/day1input.txt', 'r') as f:
            for line in f.readlines():
                l, r = line.split()
                self.left.append(int(l))
                self.right.append(int(r))
        self.left.sort()
        self.right.sort()
        self.left_counter = self._val_counter(self.left)
        self.right_counter = self._val_counter(self.right)
        self.part1 = 0
        self.part2 = 0

    def get_diff_sum(self):
        """Get the sum of the absolute differences between the two lists."""
        for i in range(len(self.left)):
            self.part1 += abs(self.left[i] - self.right[i])

    def get_similarity_score(self):
        """Get the sum of each integer in the left list multiplied by the count
        of its appearance in the right list."""
        for key, val in self.left_counter.items():
            self.part2 += key * val * self.right_counter.get(key, 0)

    def _val_counter(self, list):
        """Create a dictionary of the count of each integer in the list."""
        counts = {}
        for x in list:
            counts[x] = counts.get(x, 0) + 1
        return counts


if __name__ == '__main__':
    day1 = AdventDay1()
    day1.get_diff_sum()
    day1.get_similarity_score()
    print(day1.part1, day1.part2)
