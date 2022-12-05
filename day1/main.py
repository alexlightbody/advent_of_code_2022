
def str_to_int(l):
    return [int(x) for x in l]


def task():
    with open('day1_input.txt', 'r') as f:
        data = f.read()
        data_into_list = data.replace('\n\n', '\nx ').replace('\n', ' ').split('x')
        x = [l.strip().split(' ') for l in data_into_list]
        y = ([sum(str_to_int(l)) for l in x])
        y.sort()

        print(max(y))  # Part 1
        print(sum(y[-3:]))  # Part 2

if __name__ == '__main__':
    task()
