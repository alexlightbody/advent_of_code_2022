# A, X are Rock
# B, Y are Paper
# C, Z are Scissors

X = 1
Y = 2
Z = 3

# 6 Points if win
# 3 points if Draw
# 0 points if loss

# Losing combos:
# A Z # 3 points
# B X # 1 point
# C Y # 2 point

# Winning combos:
# A Y 8 Points
# B Z 9 Points
# C X 7 Points

# Drawing Games
# A X 4 Points
# B Y 5 Points
# C Z 6 Points

scores_map = {'A Z': 3,
          'B X': 1,
          'C Y': 2,
          'A Y': 8,
          'B Z': 9,
          'C X': 7,
          'A X': 4,
          'B Y': 5,
          'C Z': 6}

# X = Lose
# Y = Draw
# Z = Win

# A X rock, scissors. 3 points
# A Y rock, rock, 4 points
# A Z rock, paper, 8 points
# B X paper, rock 1 point
# B Y paper, paper, 5 points
# B Z paper, scissors 9 points
# C X scissors, paper, 2 points
# C Y scissors, scissors, 6 points
# C Z scissors, rock, 7 points


scores_map_2 = {'A Z': 8,
          'B X': 1,
          'C Y': 6,
          'A Y': 4,
          'B Z': 9,
          'C X': 2,
          'A X': 3,
          'B Y': 5,
          'C Z': 7}

def task():
    with open('input.txt') as f:
        to_list = f.read().split('\n')
        print(sum([scores_map.get(res) for res in to_list]))

if __name__ == '__main__':
    task()
