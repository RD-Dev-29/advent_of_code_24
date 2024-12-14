from day_starter import DayStarter


class AdventDay9:

    def __init__(self):
        self.data = DayStarter(9).split('\n')[0]
        self._process_data()
        self.part1 = 0
        self.part2 = 0

    def _process_data(self):
        self.disk_expanded = []
        self.file_map: list[dict] = []
        self.space_map: list[dict] = []
        cur_index = 0
        for i, x in enumerate(self.data):
            if i % 2 == 0:
                self.disk_expanded += [str(i//2)]*int(x)
                self.file_map.append({'id': str(i//2),
                                      'file_begin': int(cur_index),
                                      'block_count': int(x),
                                      'moved': False})
            else:
                self.disk_expanded += ['.']*int(x)
                self.space_map.append({'space_begin': int(cur_index),
                                       'block_count': int(x)})
            cur_index += int(x)

    def disk_fragment_by_block(self):
        temp = self.disk_expanded.copy()
        l, r = 0, len(temp) - 1
        while l < r:
            if temp[l] != '.':
                l += 1
            elif temp[r] == '.':
                r -= 1
            else:
                temp[l], temp[r] = temp[r], temp[l]
                l += 1
                r -= 1
        self.part1_fragment = temp

    def disk_fragment_by_file(self):
        for file in self.file_map[::-1]:
            for i, space in enumerate(self.space_map):
                if file['file_begin'] <= space['space_begin']:
                    break
                if file['block_count'] == space['block_count']:
                    self.space_map.append({'space_begin': file['file_begin'],
                                           'block_count': file['block_count']})
                    file['file_begin'] = space['space_begin']
                    self.space_map.pop(i)
                    self.space_map.sort(key=lambda x: x['space_begin'])
                    break
                elif file['block_count'] < space['block_count']:
                    self.space_map.append({'space_begin': file['file_begin'],
                                           'block_count': file['block_count']})
                    file['file_begin'] = space['space_begin']
                    space['block_count'] -= file['block_count']
                    space['space_begin'] += file['block_count']
                    self.space_map.sort(key=lambda x: x['space_begin'])
                    break

    def calc_checksum(self):
        for i, x in enumerate(self.part1_fragment):
            if x != '.':
                self.part1 += int(x)*i
        for file in self.file_map:
            self.part2 += sum([int(file['id'])*(file['file_begin'] + i)
                               for i in range(file['block_count'])])


if __name__ == '__main__':
    day9 = AdventDay9()
    day9.disk_fragment_by_block()
    day9.disk_fragment_by_file()
    day9.calc_checksum()
    print(day9.part1, day9.part2)
