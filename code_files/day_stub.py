import os


for j in range(1, 26):
    if f'day{j}.py' not in os.listdir('code_files'):
        with open(f'code_files/day{j}.py', 'w') as f:
            with open('code_files/day_n.txt', 'r') as s:
                f.write(s.read().replace('_num', str(j)))
