def task_one(stack_dict, commands):
    for c in commands:
        for _ in range(c['to_transfer']):
            # print(f"moving: {stack_dict[c['start']][-1]} to {stack_dict[c['end']]}")
            stack_dict[c['end']].append(stack_dict[c['start']][-1])
            # print(stack_dict[c['end']])
            stack_dict[c['start']].pop()
            # print(stack_dict)
    res = ''
    for r in stack_dict.values():
        res += r[-1]
    print(res)


def task_two(stack_dict, commands):
    for c in commands:
        to_move = c['to_transfer']
        stack_dict[c['end']].extend(stack_dict[c['start']][-to_move:])
        stack_dict[c['start']] = stack_dict[c['start']][:-to_move]
        # print(stack_dict)
    res = ''
    for r in stack_dict.values():
        res += r[-1]
    print(res)


if __name__ == '__main__':
    with open('input_stack.txt') as f:
        to_list = f.read().split('\n')
        stack_dict = {row[0]: list(row[1:]) for row in to_list}
        print(stack_dict)
    with open('input_instructions.txt') as i:
        cmd_list = i.read().replace('move ', '').replace('from ', '').replace('to ', '').split('\n')
        commands = [{'to_transfer': int(x.split(' ')[0]), 'start': x.split(' ')[1], 'end': x.split(' ')[2]} for x in cmd_list]
        # print(commands)

    task_one(stack_dict, commands)
    task_two(stack_dict, commands)

