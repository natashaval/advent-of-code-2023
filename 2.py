text = open('2_input.txt', 'r')
line_list = text.readlines()

sum = 0
for line in line_list:
    line = line.replace(";", ",")
    after_game = line.split(":")[1]
    game_id = int(line.split(":")[0].split(" ")[1])
    balls = after_game.split(",")
    check = True
    for ball in balls:
        # NEED to replace last \n
        ball = ball[1:].replace("\n", "").replace("\r", "")
        number = int(ball.split(" ")[0])
        color = ball.split(" ")[1]
        # print(f"ball {number} {color}")
        if (color == "red" and number > 12) or (color == "green" and number > 13) or (color == "blue" and number > 14):
            check = False
            break

    # print(f"=== turn {turn_index} check: {check}")
    if check is True:
        # print(f"+++ GAME {index + 1} last sum: {sum} \n")
        sum +=  game_id

print(sum)

# Answer: 2619 (too high)

# 1 - 25 correct
# 37 - 50 different
# 44 - 50 different
# 44 - 47 DIFFERENT 47 vs 138
# not 44, YES 45, YES 46 -> the issue is checking end of line !!!!