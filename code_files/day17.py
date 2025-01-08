from day_starter import DayStarter


class AdventDay17:

    def __init__(self):
        self.data = [x for x in DayStarter(17).split('\n') if x != '']
        self._process_data()
        self.output = []
        self.p = 0
        self._instr_map = {'0': self._adv, '1': self._bxl, '2': self._bst,
                           '3': self._jnz, '4': self._bxc, '5': self._out,
                           '6': self._bdv, '7': self._cdv}
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.A = int(self.data[0].split()[-1])
        self.B = int(self.data[1].split()[-1])
        self.C = int(self.data[2].split()[-1])
        self.instructions = [x for x in self.data[3].split(': ')[1].split(',')]

    def _operand_map(self, operand):
        if operand in '0123':
            return int(operand)
        elif operand in '456':
            return [self.A, self.B, self.C][int(operand) - 4]

    def execute_program(self, searching=False):
        while self.p < len(self.instructions):
            op, val = [self.instructions[self.p + i] for i in range(2)]
            self._instr_map[op](val)
        if not searching:
            self.part1 = ','.join([str(x) for x in self.output])

    def find_A(self):
        A = 1
        while True:
            self.A, self.p, self.B, self.C, self.output = A, 0, 0, 0, []
            self.execute_program(True)
            n = len(self.output)
            if [str(x) for x in self.output] == self.instructions:
                break
            if [str(x) for x in self.output] == self.instructions[-1*n:]:
                A <<= 3
            else:
                A += 1
        self.part2 = A

    def _adv(self, operand):
        self.A //= (2 ** self._operand_map(operand))
        self.p += 2

    def _bxl(self, operand):
        self.B ^= int(operand)
        self.p += 2

    def _bst(self, operand):
        self.B = self._operand_map(operand) % 8
        self.p += 2

    def _jnz(self, operand):
        if self.A == 0:
            self.p += 2
            return
        self.p = self._operand_map(operand)

    def _bxc(self, operand):
        self.B ^= self.C
        self.p += 2

    def _out(self, operand):
        self.output.append(self._operand_map(operand) % 8)
        self.p += 2

    def _bdv(self, operand):
        self.B = self.A // (2 ** self._operand_map(operand))
        self.p += 2

    def _cdv(self, operand):
        self.C = self.A // (2 ** self._operand_map(operand))
        self.p += 2


if __name__ == '__main__':
    day17 = AdventDay17()
    day17.execute_program()
    day17.find_A()
    print(day17.part1, day17.part2)
