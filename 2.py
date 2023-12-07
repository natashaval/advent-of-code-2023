text = open('2_input.txt', 'r')
line_list = text.readlines()

sum = 0
for index, line in enumerate(line_list):
    after_game = line.split(":")[1]
    turns = after_game.split(";")
    check = True
    for turn_index, turn in enumerate(turns):
        if check is False:
            continue

        balls = turn.split(",")
        for ball in balls:
            ball = ball[1:]
            number = int(ball.split(" ")[0])
            color = ball.split(" ")[1]
            # print(f"turn {turn_index}: ball {number} {color}")
            if (color == "red" and number > 12) or (color == "green" and number > 13) or (color == "blue" and number > 14):
                check = False
                break
        # print(f"=== turn {turn_index} check: {check}")
    if check is True:
        # print(f"+++ GAME {index + 1} last sum: {sum} \n")
        sum +=  index + 1

print(sum)

# Answer: 2619 (too high)

# 1 - 25 correct