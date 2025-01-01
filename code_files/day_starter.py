import requests
from session_cookie import session_cookie


class DayStarter:

    def __new__(self, day, micro: bool = False):
        if micro:
            with open(f'input_files/day{day}input_micro.txt', 'r') as f:
                return f.read()
        try:
            with open(f'input_files/day{day}input.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            pass
        self.day = day
        self.url = f"https://adventofcode.com/2024/day/{day}/input"
        self.cookies = {
            "session": session_cookie
        }
        self.day_input = requests.get(self.url, cookies=self.cookies)
        if self.day_input.status_code == 200:
            self.input = self.day_input.text
            with open(f'input_files/day{day}input.txt', 'w') as f:
                f.write(self.input)
            return self.input
        else:
            print("Error fetching input")


if __name__ == '__main__':
    for day in range(26):
        mgr = DayStarter(day)
