"""Day 4 of Advent of Code 2024.

The goal of part 1 is to find the number of times the word 'XMAS' appears in
the word search in a row, column, or diagonal forwards or backwards.
We can iterate over the rows, columns, and diagonals to find the words.

The goal of part 2 is to find the number of times the word 'MAS'
appears as a diagonal X in the word search.

  Valid Diagonals:
        [M . M]    [M . S]    [S . S]    [S . M]
        [. A .] or [. A .] or [. A .] or [. A .]
        [S . S]    [M . S]    [M . M]    [S . M]

We can iterate over square portions of the word search to find the indicated
valid diagonals.
"""


class AdventDay4:

    def __init__(self):
        """Initialize the word search, the row and column dimensions, and
        the goals for the word search. The word search is stored as a list of
        lists where each list is a row of the word search. The goals are the
        words 'XMAS' and 'MAS' and the words 'SAMX' and 'SAM' for part 1 and
        part 2 respectively.
        """
        self.ws = []
        with open('input_files/day4input.txt', 'r') as f:
            for line in f.readlines():
                self.ws.append([x for x in line if x != '\n'])
        self.n = len(self.ws)
        self.m = len(self.ws[0])
        self.word_goal = ['XMAS', 'SAMX']
        self.x_goal = ['MAS', 'SAM']
        self.part1 = 0
        self.part2 = 0

    def xmas_search(self):
        """Search for the word 'XMAS' in the word search."""
        self._row_search()
        self._col_search()
        self._diag_search()

    def _row_search(self):
        """Search for the word 'XMAS' in the rows of the word search."""
        for row in self.ws:
            for i in range(self.m - 3):
                self.part1 += ''.join(row[i:i+4]) in self.word_goal

    def _col_search(self):
        """Search for the word 'XMAS' in the columns of the word search."""
        for col in zip(*self.ws):
            for i in range(self.m - 3):
                self.part1 += ''.join(col[i:i+4]) in self.word_goal

    def _diag_search(self):
        """Search for the word 'XMAS' in the diagonals of the word search."""
        for row in range(self.n - 3):
            for col in range(self.m - 3):
                diag_1 = ''.join([self.ws[row][col],
                                  self.ws[row+1][col+1],
                                  self.ws[row+2][col+2],
                                  self.ws[row+3][col+3]])
                diag_2 = ''.join([self.ws[row+3][col],
                                  self.ws[row+2][col+1],
                                  self.ws[row+1][col+2],
                                  self.ws[row][col+3]])
                self.part1 += diag_1 in self.word_goal
                self.part1 += diag_2 in self.word_goal

    def diag_x_mas_search(self):
        """Search for the word 'MAS' to cross in the diagonals of the word
        search.
        """
        for row in range(self.n - 2):
            for col in range(self.m - 2):
                diag_1 = ''.join([self.ws[row][col],
                                  self.ws[row+1][col+1],
                                  self.ws[row+2][col+2]])
                diag_2 = ''.join([self.ws[row+2][col],
                                  self.ws[row+1][col+1],
                                  self.ws[row][col+2]])
                self.part2 += diag_1 in self.x_goal and diag_2 in self.x_goal


if __name__ == '__main__':
    mgr = AdventDay4()
    mgr.xmas_search()
    mgr.diag_x_mas_search()
    print(mgr.part1, mgr.part2)
