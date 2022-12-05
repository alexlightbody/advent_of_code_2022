import string

alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
alpha_values = {l: i for l, i in zip(alphabet, range(1, 53))}


def task_one(to_list):
    r1 = [s[:int(len(s)/2)] for s in to_list]
    r2 = [s[int(len(s)/2):] for s in to_list]
    sum_priorities = 0
    for r1, r2 in zip(r1, r2):
        duplicate = list(set(r1).intersection(r2))[0]
        sum_priorities += alpha_values[duplicate]
    print(sum_priorities)


def task_two(to_list):
    sum_priorities = 0
    for i in range(0, len(to_list), 3):
        group = to_list[i: i + 3]

        common_letter = list(set(group[0]).intersection(group[1]).intersection(group[2]))[0]
        sum_priorities += alpha_values[common_letter]
    print(sum_priorities)
if __name__ == '__main__':
    with open('input.txt') as f:
        to_list = f.read().split('\n')
    task_one(to_list)
    task_two(to_list)