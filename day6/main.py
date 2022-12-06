def check_marker(buffer):
    for count, letter in enumerate(buffer):
        if count >= 3:
            signal = buffer[count-3:count+1]
            if len(set(signal)) == 4:
                return count + 1


def check_message(buffer):
    for count, letter in enumerate(buffer):
        if count >= 13:
            signal = buffer[count-13:count+1]
            if len(set(signal)) == 14:
                return count + 1

if __name__ == '__main__':
    with open('input.txt') as f:
        buffer = f.read()
        print(buffer)
    #Task 1
    print(check_marker(buffer))
    #Task 2
    print(check_message(buffer))
