
def check_enclosed(a1_low, a1_high, a2_low, a2_high):
    return (a2_low >= a1_low) & (a2_high <= a1_high) or (a1_low >= a2_low) & (a1_high <= a2_high)


def check_some_overlap(a1_low, a1_high, a2_low, a2_high):
    return (((a2_low >= a1_low) & (a2_low <= a1_high)) or ((a2_high <= a1_high) & (a2_high >= a1_low))) or (((a1_low >= a2_low) & (a1_low <= a2_high)) or ((a1_high <= a2_high) & (a1_high >= a2_low)))


if __name__ == '__main__':
    with open('input.txt') as f:
        to_list = f.read().split('\n')
    count_full_contained = 0
    count_partial_contained = 0
    for r in to_list:
        a1, a2 = r.split(',')
        a1_low, a1_high = map(int,a1.split('-'))
        a2_low, a2_high = map(int,a2.split('-'))
        if check_enclosed(a1_low, a1_high, a2_low, a2_high):
            count_full_contained += 1
        if check_some_overlap(a1_low, a1_high, a2_low, a2_high):
            count_partial_contained += 1
        # print(r, a1_low, a1_high, a2_low, a2_high, check_enclosed(a1_low, a1_high, a2_low, a2_high))

    print('count_full_contained: ', count_full_contained)
    print('count_partial_contained: ', count_partial_contained)
#603 too high
#564 too low

#583 Part 1 (Issue was needed to convert to int)
#983 Part 2
